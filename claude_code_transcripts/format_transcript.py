#!/usr/bin/env python3
"""
Format a Claude Code raw transcript JSONL file into a CLI-style transcript.

- User inputs are shown with > prefix
- Claude actions are shown with ⏺ prefix
- Write actions show at most 10 lines with "… +N lines" for longer content
- Read/Edit actions show result info (line counts, additions/removals)
- Text feedback to the user is shown in full
"""

import json
import sys
import os
import re


def format_write_content(content: str, max_lines: int = 10) -> str:
    """Format file content, truncating if more than max_lines."""
    lines = content.split('\n')
    if len(lines) <= max_lines:
        return content

    shown_lines = '\n'.join(lines[:max_lines])
    remaining = len(lines) - max_lines
    return f"{shown_lines}\n… +{remaining} lines"


def count_lines_in_read_result(result: str) -> int:
    """Count lines from a Read tool result (format: '   123→content')."""
    if not result:
        return 0
    lines = result.strip().split('\n')
    # Find the last line number
    max_line = 0
    for line in lines:
        match = re.match(r'\s*(\d+)→', line)
        if match:
            max_line = max(max_line, int(match.group(1)))
    return max_line


def format_unified_diff(old_str: str, new_str: str) -> str:
    """Create a unified diff-style output for an edit."""
    import difflib

    old_lines = old_str.split('\n') if old_str else []
    new_lines = new_str.split('\n') if new_str else []

    diff_lines = []
    matcher = difflib.SequenceMatcher(None, old_lines, new_lines)

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            # Show context (but limit it)
            context_lines = old_lines[i1:i2]
            if len(context_lines) <= 3:
                for line in context_lines:
                    diff_lines.append(f"  {line}")
            else:
                # Show first and last line with ellipsis
                diff_lines.append(f"  {context_lines[0]}")
                diff_lines.append(f"  ... ({len(context_lines) - 2} unchanged lines)")
                diff_lines.append(f"  {context_lines[-1]}")
        elif tag == 'replace':
            for line in old_lines[i1:i2]:
                diff_lines.append(f"- {line}")
            for line in new_lines[j1:j2]:
                diff_lines.append(f"+ {line}")
        elif tag == 'delete':
            for line in old_lines[i1:i2]:
                diff_lines.append(f"- {line}")
        elif tag == 'insert':
            for line in new_lines[j1:j2]:
                diff_lines.append(f"+ {line}")

    return '\n'.join(diff_lines)


def format_tool_use(tool_name: str, tool_input: dict, tool_result: str = None) -> str:
    """Format a tool use with result info."""
    if tool_name == 'Write':
        file_path = tool_input.get('file_path', '')
        content = tool_input.get('content', '')
        filename = os.path.basename(file_path)
        line_count = len(content.split('\n'))
        formatted_content = format_write_content(content)
        return f"⏺ Write({filename})\n{formatted_content}"

    elif tool_name == 'Edit':
        file_path = tool_input.get('file_path', '')
        filename = os.path.basename(file_path)
        old_str = tool_input.get('old_string', '')
        new_str = tool_input.get('new_string', '')

        diff_output = format_unified_diff(old_str, new_str)

        return f"⏺ Update({filename})\n{diff_output}"

    elif tool_name == 'Read':
        file_path = tool_input.get('file_path', '')
        filename = os.path.basename(file_path)

        if tool_result:
            line_count = count_lines_in_read_result(tool_result)
            return f"⏺ Read({filename})\n  ⎿  Read {line_count} lines"
        else:
            return f"⏺ Read({filename})"

    elif tool_name == 'TodoWrite':
        todos = tool_input.get('todos', [])
        in_progress = [t for t in todos if t.get('status') == 'in_progress']
        if in_progress:
            active = in_progress[0].get('activeForm', in_progress[0].get('content', ''))
            return f"⏺ {active}"
        return "⏺ Updating todo list"

    elif tool_name == 'Bash':
        command = tool_input.get('command', '')
        cmd_preview = command[:60] + ('...' if len(command) > 60 else '')
        return f"⏺ Bash: {cmd_preview}"

    elif tool_name == 'Grep':
        pattern = tool_input.get('pattern', '')
        return f"⏺ Grep: {pattern}"

    elif tool_name == 'Glob':
        pattern = tool_input.get('pattern', '')
        return f"⏺ Glob: {pattern}"

    else:
        return f"⏺ {tool_name}"


def format_transcript(jsonl_path: str) -> str:
    """Convert a JSONL transcript to CLI-style format."""
    output_lines = []

    with open(jsonl_path, 'r') as f:
        entries = [json.loads(line) for line in f]

    # First pass: collect tool results by tool_use_id
    tool_results = {}
    for entry in entries:
        if entry.get('type') == 'user':
            msg = entry.get('message', {})
            content = msg.get('content')
            if isinstance(content, list):
                for item in content:
                    if item.get('type') == 'tool_result':
                        tool_id = item.get('tool_use_id')
                        result_content = item.get('content', '')
                        if tool_id:
                            tool_results[tool_id] = result_content

    # Second pass: format the transcript
    for entry in entries:
        entry_type = entry.get('type')

        if entry_type == 'file-history-snapshot':
            # Skip file history snapshots
            continue

        elif entry_type == 'user':
            msg = entry.get('message', {})
            content = msg.get('content')

            # Handle string content (actual user input)
            if isinstance(content, str):
                # User message - show with > prefix
                # Strip the leading > if present in the stored message
                user_text = content.strip()
                if user_text.startswith('>'):
                    user_text = user_text[1:].strip()
                output_lines.append(f"> {user_text}")
                output_lines.append("")

            # Skip tool_result content (internal system responses)
            elif isinstance(content, list):
                # This is a tool result, skip it
                pass

        elif entry_type == 'assistant':
            msg = entry.get('message', {})
            content = msg.get('content', [])

            for item in content:
                item_type = item.get('type')

                if item_type == 'text':
                    # Assistant text - show in full
                    text = item.get('text', '')
                    if text.strip():
                        output_lines.append(text)
                        output_lines.append("")

                elif item_type == 'tool_use':
                    # Tool use - format with result info
                    tool_name = item.get('name', '')
                    tool_input = item.get('input', {})
                    tool_id = item.get('id', '')
                    tool_result = tool_results.get(tool_id)

                    formatted = format_tool_use(tool_name, tool_input, tool_result)
                    output_lines.append(formatted)
                    output_lines.append("")

    return '\n'.join(output_lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python format_transcript.py <transcript.jsonl> [output.txt]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    transcript = format_transcript(input_path)

    if output_path:
        with open(output_path, 'w') as f:
            f.write(transcript)
        print(f"Transcript written to {output_path}")
    else:
        print(transcript)


if __name__ == '__main__':
    main()
