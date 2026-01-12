library(tidyverse)
library(ggplot2)

# Read the results
df <- read_csv("results_cn/results.csv")

# Calculate success rate per model/effort/num combination
# Success = is_checkmate is TRUE
success_df <- df %>%
  group_by(model, effort, num_requested) %>%
  summarize(
    n_scenarios = n(),
    n_success = sum(is_checkmate, na.rm = TRUE),
    success_rate = n_success / n_scenarios,
    .groups = "drop",
    reasoning_length_per = sum(reasoning_length) / n_scenarios,
  )

# Plot 1: Success rate as a function of num for selected models (effort varies)
# Models: anthropic/claude-opus-4.5, google/gemini-3-pro-preview, openai/gpt-5.1
plot1_models <- c("anthropic/claude-opus-4.5", "google/gemini-3-pro-preview", "openai/gpt-5.1")

p1 <- success_df %>%
  filter(model %in% plot1_models, effort == "high") %>%
  ggplot(aes(x = model, y = success_rate, fill = as.factor(num_requested))) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer() +
  labs(
    title = "Success Rate by Number of Scenarios Requested",
    subtitle = "Effort = high",
    x = "Model",
    y = "Success Rate",
    fill = "Number of Scenarios Requested"
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 8)
  )
p1

ggsave("results_cn/plot1_success_by_num.png", p1, width = 8, height = 6, dpi = 150)

p15 <- success_df %>%
  filter(model %in% plot1_models, effort == "high") %>%
  ggplot(aes(x = model, y = reasoning_length_per, fill = as.factor(num_requested))) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous() +
  scale_fill_brewer() +
  labs(
    title = "Completion length per scenario requested",
    subtitle = "Effort = high",
    x = "Model",
    y = "Completion tokens",
    fill = "Number of Scenarios Requested"
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 8)
  )
p15
ggsave("results_cn/plot15_reasoning_length.png", p15, width = 8, height = 6, dpi = 150)

# Plot 2: Success rate as a function of effort for num = 3
# Models: anthropic/claude-sonnet-4.5, anthropic/claude-opus-4.5, google/gemini-3-pro-preview, openai/gpt-5.1
plot2_models <- c("anthropic/claude-sonnet-4.5", "anthropic/claude-opus-4.5",
                  "google/gemini-3-pro-preview", "openai/gpt-5.1")

effort_order <- c("none", "low", "medium", "high")

p2 <- success_df %>%
  filter(model %in% plot2_models, num_requested == 3) %>%
  mutate(effort = factor(effort, levels = effort_order)) %>%
  ggplot(aes(x = model, y = success_rate, fill = effort)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer() +
  labs(
    title = "Success Rate by Reasoning Effort Level",
    subtitle = "Number of scenarios = 3",
    fill = "Reasoning Effort Level",
    y = "Success Rate",
    x = "Model"
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 8)
  )
p2

ggsave("results_cn/plot2_success_by_effort.png", p2, width = 8, height = 6, dpi = 150)

# Plot 3: Success rate for all models with effort=high, num=3
p3 <- success_df %>%
  filter(effort == "high", num_requested == 3) %>%
  ggplot(aes(x = reorder(model, success_rate), y = success_rate, fill = model)) +
  geom_bar(stat = "identity", width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Success Rate by Model",
    subtitle = "Effort = high, Number of scenarios = 3",
    x = "Model",
    y = "Success Rate",
    fill = "Model"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none"
  ) +
  coord_flip()
p3

ggsave("results_cn/plot3_success_all_models.png", p3, width = 8, height = 6, dpi = 150)

# ============================================================================
# Plots 4-6: Perfect run rate (all scenarios pass in a run)
# ============================================================================

# Calculate perfect run rate: % of runs where ALL scenarios pass
perfect_run_df <- df %>%
  group_by(model, effort, num_requested, run) %>%
  summarize(
    all_pass = all(is_checkmate, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  group_by(model, effort, num_requested) %>%
  summarize(
    n_runs = n(),
    n_perfect = sum(all_pass),
    perfect_rate = n_perfect / n_runs,
    .groups = "drop"
  )

# Plot 4: Perfect run rate as a function of num for selected models
p4 <- perfect_run_df %>%
  filter(model %in% plot1_models, effort == "high") %>%
  ggplot(aes(x = model, y = perfect_rate, fill = as.factor(num_requested))) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer() +
  labs(
    title = "Perfect Run Rate by Number of Scenarios Requested",
    subtitle = "Effort = high (all scenarios must pass)",
    x = "Model",
    y = "Perfect Run Rate",
    fill = "Number of Scenarios Requested"
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 8)
  )
p4

ggsave("results_cn/plot4_perfect_by_num.png", p4, width = 8, height = 6, dpi = 150)

# Plot 5: Perfect run rate as a function of effort for num = 3
p5 <- perfect_run_df %>%
  filter(model %in% plot2_models, num_requested == 3) %>%
  mutate(effort = factor(effort, levels = effort_order)) %>%
  ggplot(aes(x = model, y = perfect_rate, fill = effort)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer() +
  labs(
    title = "Perfect Run Rate by Reasoning Effort Level",
    subtitle = "Number of scenarios = 3 (all scenarios must pass)",
    fill = "Reasoning Effort Level",
    y = "Perfect Run Rate",
    x = "Model"
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 8)
  )
p5

ggsave("results_cn/plot5_perfect_by_effort.png", p5, width = 8, height = 6, dpi = 150)

# Plot 6: Perfect run rate for all models with effort=high, num=3
p6 <- perfect_run_df %>%
  filter(effort == "high", num_requested == 3) %>%
  ggplot(aes(x = reorder(model, perfect_rate), y = perfect_rate, fill = model)) +
  geom_bar(stat = "identity", width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    title = "Perfect Run Rate by Model",
    subtitle = "Effort = high, Number of scenarios = 3 (all scenarios must pass)",
    x = "Model",
    y = "Perfect Run Rate",
    fill = "Model"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none"
  ) +
  coord_flip()
p6

ggsave("results_cn/plot6_perfect_all_models.png", p6, width = 8, height = 6, dpi = 150)

print("Plots saved: plot1_success_by_num.png, plot2_success_by_effort.png, plot3_success_all_models.png")
print("             plot4_perfect_by_num.png, plot5_perfect_by_effort.png, plot6_perfect_all_models.png")

# ============================================================================
# Plots 7-9: Perfect run rate vs expected (binomial model)
# ============================================================================

# Join perfect run rate with individual success rate to compute expected
# Expected perfect rate under independence = p^num
comparison_df <- perfect_run_df %>%
  left_join(success_df, by = c("model", "effort", "num_requested")) %>%
  mutate(
    expected_perfect_rate = success_rate ^ num_requested
  )

# Reshape for plotting observed vs expected
comparison_long <- comparison_df %>%
  select(model, effort, num_requested, perfect_rate, expected_perfect_rate) %>%
  pivot_longer(
    cols = c(perfect_rate, expected_perfect_rate),
    names_to = "type",
    values_to = "rate"
  ) %>%
  mutate(
    type = ifelse(type == "perfect_rate", "Observed", "Expected (p^n)")
  )

# Plot 7: Observed vs expected perfect rate by num
p7 <- comparison_long %>%
  filter(model %in% plot1_models, effort == "high") %>%
  ggplot(aes(x = model, y = rate, fill = interaction(as.factor(num_requested), type))) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_manual(
    values = c(
      "3.Observed" = "#1b9e77", 
      "5.Observed" = "#d95f02", 
      "7.Observed" = "#7570b3", 
      "10.Observed" = "#666666", 
      "3.Expected (p^n)" = "#a6dba0",
      "5.Expected (p^n)" = "#fdae61",
      "7.Expected (p^n)" = "#bcbddc",
      "10.Expected (p^n)" = "#aaaaaa"
    ),
    labels = c(
      "3.Observed" = "n=3 Observed", 
      "5.Observed" = "n=5 Observed", 
      "7.Observed" = "n=7 Observed", 
      "10.Observed" = "n=10 Observed", 
      "3.Expected (p^n)" = "n=3 Expected",
      "5.Expected (p^n)" = "n=5 Expected",
      "7.Expected (p^n)" = "n=7 Expected",
      "10.Expected (p^n)" = "n=10 Expected"
    )
  ) +
  labs(
    title = "Perfect Run Rate: Observed vs Expected (Binomial)",
    subtitle = "Effort = high; Expected = p^n assuming independence",
    x = "Model",
    y = "Perfect Run Rate",
    fill = ""
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 8)
  )
p7

ggsave("results_cn/plot7_perfect_vs_expected_by_num.png", p7, width = 10, height = 6, dpi = 150)

# Plot 8: Observed vs expected perfect rate by effort for num = 3
p8 <- comparison_long %>%
  filter(model %in% plot2_models, num_requested == 3) %>%
  mutate(effort = factor(effort, levels = effort_order)) %>%
  ggplot(aes(x = model, y = rate, fill = interaction(effort, type))) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_manual(
    values = c(
      "none.Observed" = "#1b9e77", "none.Expected (p^n)" = "#a6dba0",
      "low.Observed" = "#d95f02", "low.Expected (p^n)" = "#fdae61",
      "medium.Observed" = "#7570b3", "medium.Expected (p^n)" = "#bcbddc",
      "high.Observed" = "#e7298a", "high.Expected (p^n)" = "#f1b6da"
    ),
    labels = c(
      "none.Observed" = "none Obs", "none.Expected (p^n)" = "none Exp",
      "low.Observed" = "low Obs", "low.Expected (p^n)" = "low Exp",
      "medium.Observed" = "med Obs", "medium.Expected (p^n)" = "med Exp",
      "high.Observed" = "high Obs", "high.Expected (p^n)" = "high Exp"
    )
  ) +
  labs(
    title = "Perfect Run Rate: Observed vs Expected (Binomial)",
    subtitle = "Number of scenarios = 3; Expected = p^3 assuming independence",
    fill = "",
    y = "Perfect Run Rate",
    x = "Model"
  ) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 8)
  )
p8

ggsave("results_cn/plot8_perfect_vs_expected_by_effort.png", p8, width = 10, height = 6, dpi = 150)

# Plot 9: Observed vs expected for all models with effort=high, num=3
p9 <- comparison_long %>%
  filter(effort == "high", num_requested == 3) %>%
  ggplot(aes(x = reorder(model, rate), y = rate, fill = type)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  scale_y_continuous(labels = scales::percent, limits = c(0, 1)) +
  scale_fill_manual(values = c("Observed" = "#1b9e77", "Expected (p^n)" = "#a6dba0")) +
  labs(
    title = "Perfect Run Rate: Observed vs Expected (Binomial)",
    subtitle = "Effort = high, Number of scenarios = 3; Expected = p^3 assuming independence",
    x = "Model",
    y = "Perfect Run Rate",
    fill = ""
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  ) +
  coord_flip()
p9

ggsave("results_cn/plot9_perfect_vs_expected_all_models.png", p9, width = 8, height = 6, dpi = 150)

print("             plot7_perfect_vs_expected_by_num.png, plot8_perfect_vs_expected_by_effort.png, plot9_perfect_vs_expected_all_models.png")

# ============================================================================
# Plots 10-14: Analysis of results/scores.csv
# UI, Logic, and Aggregate scores by model
# ============================================================================

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

pval_two_sided <- function(k1, N1, k2, N2) {
  tab <- matrix(
    c(k1, N1 - k1,
      k2, N2 - k2),
    nrow = 2,
    byrow = TRUE,
    dimnames = list(
      group   = c("group1", "group2"),
      outcome = c("success", "failure")
    )
  )
  
  fisher.test(tab, alternative = "two.sided")$p.value
}

success_df %>% filter(effort == "high", num_requested == 3)
# anthropic/claude-opus-4.5
pval_two_sided(22, 30, 23, 30)

# anthropic/claude-sonnet-4.5
pval_two_sided(5, 30, 14, 30)

# google/gemini-3-pro-preview
pval_two_sided(27, 30, 22, 30)

# openai/gpt-5.1
pval_two_sided(25, 30, 20, 30)



## Distribution of completion time T = max(G1, ..., GN)
## where Gi ~ Geom(p) (support: 1,2,...)

# pmf of T at t
pmf_T <- function(t, N, p) {
  cdf_t   <- (1 - (1 - p)^t)^N
  cdf_tm1 <- (1 - (1 - p)^(t - 1))^N
  cdf_t - cdf_tm1
}

# cdf of T at t
cdf_T <- function(t, N, p) {
  (1 - (1 - p)^t)^N
}

# helper to make a data.frame over a reasonable t grid
make_T_dist <- function(N, p, tail_prob_cutoff = 1e-6, t_max_cap = 1000) {
  # grow t until CDF ~ 1 or hit cap
  t_vals <- 1:t_max_cap
  cdf_vals <- cdf_T(t_vals, N, p)
  # find last t where CDF < 1 - tail_prob_cutoff
  if (all(cdf_vals < 1 - tail_prob_cutoff)) {
    t_max <- t_max_cap
  } else {
    t_max <- min(which(cdf_vals >= 1 - tail_prob_cutoff))
  }
  t_vals <- 1:t_max
  
  pmf_vals <- pmf_T(t_vals, N, p)
  cdf_vals <- cdf_T(t_vals, N, p)
  
  data.frame(t = t_vals, pmf = pmf_vals, cdf = cdf_vals)
}

## Example usage: N = 5 slots, p = 0.3 per slot per round
N <- 5
p <- 0.56

dist_T <- make_T_dist(N, p)

# Plot PMF
plot(dist_T$t, dist_T$pmf, type = "h",
     main = sprintf("PMF of completion time T (N=%d, p=%.2f)", N, p),
     xlab = "t (rounds)", ylab = "P(T = t)")

# Optionally add points on top
points(dist_T$t, dist_T$pmf, pch = 16)

# Plot CDF
plot(dist_T$t, dist_T$cdf, type = "s",
     main = sprintf("CDF of completion time T (N=%d, p=%.2f)", N, p),
     xlab = "t (rounds)", ylab = "P(T ≤ t)")


# ============================================================================
# Plots for iterative benchmark (results_cni)
# ============================================================================

# Read iterative benchmark results
cni_df <- read_csv("results_cni/results.csv")

# Calculate expected iterations using the T distribution
# E[T] = sum(t * P(T = t)) where T = max(G1, ..., GN), Gi ~ Geom(p)
expected_T <- function(N, p) {
  if (is.na(p) || is.na(N)) return(NA)
  if (p <= 0 || p >= 1) return(NA)
  dist <- make_T_dist(N, p)
  sum(dist$t * dist$pmf)
}

# Get success rates from the non-iterative benchmark (success_df)
# Match by model and num_requested, use effort = "high"
success_rates <- success_df %>%
  filter(effort == "high") %>%
  select(model, num_requested, success_rate)

# Join with iterative results
cni_with_expected <- cni_df %>%
  left_join(success_rates, by = c("model", "num_requested")) %>%
  rowwise() %>%
  mutate(
    expected_iterations = expected_T(num_requested, success_rate)
  ) %>%
  ungroup()

# Plot 16: Dotplot of iterations by model and num_requested
# with expected value line
p16 <- cni_with_expected %>%
  mutate(num_requested = as.factor(num_requested)) %>%
  ggplot(aes(x = model, y = num_iterations)) +
  geom_jitter(aes(color = num_requested), width = 0.2, height = 0, alpha = 0.7, size = 3) +
  geom_point(aes(y = expected_iterations, shape = num_requested),
             size = 4, color = "black", stroke = 1.5) +
  scale_y_continuous(limits = c(0, NA)) +
  scale_color_brewer(palette = "Set1") +
  labs(
    title = "Iterations to Convergence (Iterative Benchmark)",
    subtitle = "Dots = observed runs, shapes = expected E[T] from geometric model",
    x = "Model",
    y = "Number of Iterations",
    color = "Num Requested",
    shape = "Num Requested (Expected)"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom"
  )
p16

ggsave("results_cni/plot16_iterations_dotplot.png", p16, width = 10, height = 6, dpi = 150)

# Calculate expected iterations for full redraw model
# Each iteration succeeds with probability p^N (all N scenarios must be valid)
# This is a geometric distribution with success prob p^N
# E[Geom(q)] = 1/q where q = p^N
expected_T_full_redraw <- function(N, p) {
  if (is.na(p) || is.na(N)) return(NA)
  if (p <= 0 || p >= 1) return(NA)
  q <- p^N
  if (q <= 0) return(NA)
  1 / q
}

# Add full redraw expected iterations to the data
cni_with_expected <- cni_with_expected %>%
  rowwise() %>%
  mutate(
    expected_iterations_full_redraw = expected_T_full_redraw(num_requested, success_rate)
  ) %>%
  ungroup()

# Plot 17: Faceted by num_requested for clearer comparison
# with per-model horizontal lines for expected values
# First, get unique expected values per model/num_requested
expected_lines <- cni_with_expected %>%
  group_by(model, num_requested) %>%
  summarize(expected_iterations = first(expected_iterations), .groups = "drop")

p17 <- cni_with_expected %>%
  ggplot(aes(x = model, y = num_iterations)) +
  geom_jitter(width = 0.15, height = 0, alpha = 0.7, size = 3, color = "#1b9e77") +
  geom_errorbar(data = expected_lines,
                aes(y = expected_iterations, ymin = expected_iterations, ymax = expected_iterations),
                width = 0.5, color = "black", linewidth = 0.5) +
  facet_wrap(~num_requested, labeller = labeller(num_requested = function(x) paste("N =", x))) +
  scale_y_continuous(limits = c(0, NA)) +
  labs(
    title = "Iterations to Convergence by Number of Scenarios",
    subtitle = "Green dots = observed, black line = E[max(Gi)] from geometric model",
    x = "Model",
    y = "Number of Iterations"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    strip.text = element_text(face = "bold")
  )
p17

ggsave("results_cni/plot17_iterations_faceted.png", p17, width = 12, height = 6, dpi = 150)

# Plot 18: Summary with mean observed vs expected
cni_summary <- cni_with_expected %>%
  group_by(model, num_requested) %>%
  summarize(
    mean_iterations = mean(num_iterations),
    sd_iterations = sd(num_iterations),
    expected_iterations = first(expected_iterations),
    n_runs = n(),
    .groups = "drop"
  )

cni_summary_long <- cni_summary %>%
  pivot_longer(
    cols = c(mean_iterations, expected_iterations),
    names_to = "type",
    values_to = "iterations"
  ) %>%
  mutate(
    type = factor(type,
                  levels = c("mean_iterations", "expected_iterations"),
                  labels = c("Observed Mean", "Expected (Geometric)"))
  )

p18 <- cni_summary_long %>%
  ggplot(aes(x = model, y = iterations, fill = type)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8), width = 0.7) +
  facet_wrap(~num_requested, labeller = labeller(num_requested = function(x) paste("N =", x))) +
  scale_fill_manual(values = c("Observed Mean" = "#1b9e77", "Expected (Geometric)" = "#d95f02")) +
  labs(
    title = "Mean Iterations: Observed vs Expected (Geometric Model)",
    subtitle = "Expected = E[max(G1,...,GN)] where Gi ~ Geom(p), p = single-shot success rate",
    x = "Model",
    y = "Mean Iterations",
    fill = ""
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "bottom",
    strip.text = element_text(face = "bold")
  )
p18

ggsave("results_cni/plot18_iterations_observed_vs_expected.png", p18, width = 12, height = 6, dpi = 150)

print("Iterative benchmark plots saved:")
print("  results_cni/plot16_iterations_dotplot.png")
print("  results_cni/plot17_iterations_faceted.png")
print("  results_cni/plot18_iterations_observed_vs_expected.png")

