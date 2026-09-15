# Plots for the app-generation benchmark (results/scores.csv).
# Run from inside bench/. Requires the tidyverse.

library(tidyverse)
library(ggplot2)


scores <- read_csv("results/scores.csv")

# Compute derived metrics per run
scores <- scores %>%
  mutate(
    # UI: board rendered correctly, drag and drop works, no integrity stripping needed
    ui = board_correct & drag_drop_works & !needs_integrity_stripped,
    # Logic: all 3 scenarios valid, scenarios distinct, checkmate logic valid
    logic = scenario_1_valid & scenario_2_valid & scenario_3_valid &
            scenarios_distinct & checkmate_logic_valid,
    # Aggregate: both UI and logic pass
    aggregate = ui & logic,
    # All scenarios valid (just the 3 scenarios, not the other logic checks)
    all_scenarios_valid = scenario_1_valid & scenario_2_valid & scenario_3_valid
  )

# Aggregate by model
scores_by_model <- scores %>%
  group_by(model) %>%
  summarize(
    n_runs = n(),
    # Percentage of individual scenarios that are valid
    pct_scenarios_valid = mean(c(scenario_1_valid, scenario_2_valid, scenario_3_valid), na.rm = TRUE),
    # Alternative: use valid_scenario_count / (num * n_runs)
    total_scenarios = sum(num),
    total_valid_scenarios = sum(valid_scenario_count),
    scenario_pass_rate = total_valid_scenarios / total_scenarios,
    # Percentage of runs where all scenarios are valid
    pct_all_scenarios_valid = mean(all_scenarios_valid, na.rm = TRUE),
    # UI pass rate
    ui_rate = mean(ui, na.rm = TRUE),
    # Logic pass rate
    logic_rate = mean(logic, na.rm = TRUE),
    # Aggregate pass rate
    aggregate_rate = mean(aggregate, na.rm = TRUE),
    .groups = "drop"
  )

# Reshape for plotting
scores_long <- scores_by_model %>%
  select(model, scenario_pass_rate, pct_all_scenarios_valid, ui_rate, logic_rate, aggregate_rate) %>%
  pivot_longer(
    cols = c(scenario_pass_rate, pct_all_scenarios_valid, ui_rate, logic_rate, aggregate_rate),
    names_to = "metric",
    values_to = "rate"
  ) %>%
  mutate(
    metric = factor(metric,
      levels = c("scenario_pass_rate", "pct_all_scenarios_valid", "logic_rate", "ui_rate", "aggregate_rate"),
      labels = c("Individual Scenario Pass Rate", " % All Scenarios Valid", "Logic", "UI", "Total Pass Rate")
    )
  )

# Plot 10: All metrics by model (grouped bar chart)
p10 <- scores_long %>%
  ggplot(aes(x = model, y = rate, fill = metric)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Chess Benchmark Scores by Model",
    x = "Model",
    y = "Pass Rate",
    fill = "Metric"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  )
p10

ggsave("results/plot10_scores_by_model.png", p10, width = 10, height = 6, dpi = 150)

# Plot 11: UI, Logic, Aggregate only (cleaner comparison)
p11 <- scores_long %>%
  filter(metric %in% c("UI", "Logic", "Aggregate")) %>%
  ggplot(aes(x = model, y = rate, fill = metric)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_manual(values = c("UI" = "#66c2a5", "Logic" = "#fc8d62", "Aggregate" = "#8da0cb")) +
  labs(
    title = "UI, Logic, and Aggregate Scores by Model",
    subtitle = "Aggregate requires both UI and Logic to pass",
    x = "Model",
    y = "Pass Rate",
    fill = "Metric"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  )
p11

ggsave("results/plot11_ui_logic_aggregate.png", p11, width = 10, height = 6, dpi = 150)

# Plot 12: Scenario pass rates (individual vs all)
p12 <- scores_long %>%
  filter(metric %in% c("Individual Scenario Pass Rate", " % All Scenarios Valid")) %>%
  ggplot(aes(x = model, y = rate, fill = metric)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_manual(values = c("Individual Scenario Pass Rate" = "#a6d854", " % All Scenarios Valid" = "#e78ac3")) +
  labs(
    title = "Scenario Validity by Model",
    subtitle = "Individual scenario pass rate vs runs with all 3 scenarios valid",
    x = "Model",
    y = "Pass Rate",
    fill = "Metric"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  )
p12

ggsave("results/plot12_scenario_rates.png", p12, width = 10, height = 6, dpi = 150)

# Plot 13: Aggregate score only (horizontal bar, sorted)
p13 <- scores_by_model %>%
  ggplot(aes(x = reorder(model, aggregate_rate), y = aggregate_rate, fill = model)) +
  geom_bar(stat = "identity", width = 0.7) +
  geom_text(aes(label = scales::percent(aggregate_rate, accuracy = 1)),
            hjust = -0.1, size = 3.5) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1.1)) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Aggregate Score by Model",
    subtitle = "Requires both UI (board + drag/drop) and Logic (all scenarios valid + distinct + checkmate logic)",
    x = "Model",
    y = "Aggregate Pass Rate"
  ) +
  theme_minimal() +
  theme(
    legend.position = "none"
  ) +
  coord_flip()
p13

ggsave("results/plot13_aggregate_ranked.png", p13, width = 10, height = 6, dpi = 150)

# Plot 14: Faceted view of all metrics
p14 <- scores_long %>%
  ggplot(aes(x = reorder(model, rate), y = rate, fill = model)) +
  geom_bar(stat = "identity", width = 0.7) +
  facet_wrap(~metric, ncol = 3) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Chess Benchmark: All Metrics by Model",
    x = "Model",
    y = "Pass Rate"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none",
    strip.text = element_text(face = "bold")
  )
p14

ggsave("results/plot14_all_metrics_faceted.png", p14, width = 12, height = 8, dpi = 150)

print("Scores plots saved:")
print("  results/plot10_scores_by_model.png")
print("  results/plot11_ui_logic_aggregate.png")
print("  results/plot12_scenario_rates.png")
print("  results/plot13_aggregate_ranked.png")
print("  results/plot14_all_metrics_faceted.png")
