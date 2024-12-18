library(readr)
library(dplyr)
library(ggplot2)
library(tidyr)
library(gridExtra)
library(corrplot)
library(broom)
library(zoo)
library(RcppRoll)

# importing

mortality_data <- read_csv("clean_mortality_data.csv")

# clean column names

colnames(mortality_data) <- gsub(" ", "_", colnames(mortality_data))
colnames(mortality_data) <- gsub("-", "_", colnames(mortality_data))
colnames(mortality_data) <- gsub("/", "_", colnames(mortality_data))

# check for missing data

missing_summary <- colSums(is.na(mortality_data))
print(missing_summary)

# advanced statistical analysis

## correlation matrix for numeric variables
numeric_vars <- mortality_data %>% select(where(is.numeric))
cor_matrix <- cor(numeric_vars, use = "complete.obs")

# plot correlation matrix

corrplot(cor_matrix, method = "color", type = "upper", title = "Correlation Matrix", tl.col = "black")

## linear regression: co-morbidity count as dependent variable

lm_model <- lm(Co_morbidity_Count ~ Age + Socioeconomic_Index + Gender, data = mortality_data)
summary(lm_model)

# residual diagnostics

par(mfrow = c(2, 2))
plot(lm_model)
par(mfrow = c(1, 1))

## anova for co-morbidity count by age group

anova_result <- aov(Co_morbidity_Count ~ Age_Group, data = mortality_data)
anova_summary <- summary(anova_result)
print(anova_summary)

# advanced mathematical methods

## time-series decomposition

mortality_data <- mortality_data %>% mutate(date = as.Date(paste(Year, Month, "01", sep = "-")))
time_series <- mortality_data %>% 
  group_by(date) %>% 
  summarise(total_deaths = n(), .groups = "drop")

ts_data <- ts(time_series$total_deaths, start = c(min(format(time_series$date, "%Y")), 1), frequency = 12)
decomp <- decompose(ts_data)
plot(decomp)

## moving average for trend analysis

time_series <- time_series %>% 
  mutate(rolling_avg = zoo::rollmean(total_deaths, k = 3, fill = NA))

# plot time-series trends

ggplot(time_series, aes(x = date)) +
  geom_line(aes(y = total_deaths), color = "blue", alpha = 0.6) +
  geom_line(aes(y = rolling_avg), color = "red", size = 1) +
  labs(title = "Time-Series Trend Analysis", x = "Time", y = "Total Deaths") +
  theme_minimal()

# visualization-driven insights

## boxplot: socioeconomic index by gender

ggplot(mortality_data, aes(x = Gender, y = Socioeconomic_Index, fill = Gender)) +
  geom_boxplot(alpha = 0.6) +
  labs(title = "Socioeconomic Index by Gender", x = "Gender", y = "Socioeconomic Index") +
  theme_minimal()

## scatter plot: co-morbidity count vs socioeconomic index by age group

ggplot(mortality_data, aes(x = Socioeconomic_Index, y = Co_morbidity_Count, color = Age_Group)) +
  geom_point(alpha = 0.6) +
  labs(title = "Co-Morbidity Count vs Socioeconomic Index", x = "Socioeconomic Index", y = "Co-Morbidity Count") +
  theme_minimal()

# data pipeline optimization

## select and filter relevant columns for efficiency

optimized_data <- mortality_data %>% 
  select(Age, Gender, Socioeconomic_Index, Co_morbidity_Count, Infant_Death_Flag) %>%
  filter(!is.na(Socioeconomic_Index), !is.na(Co_morbidity_Count))

## use efficient summarization techniques

summary_data <- optimized_data %>% 
  group_by(Gender) %>% 
  summarise(
    avg_age = mean(Age, na.rm = TRUE),
    avg_socioeconomic_index = mean(Socioeconomic_Index, na.rm = TRUE),
    avg_co_morbidity_count = mean(Co_morbidity_Count, na.rm = TRUE),
    .groups = "drop"
  )

print(summary_data)

## save optimized outputs

write_csv(optimized_data, "optimized_mortality_data.csv")
write_csv(summary_data, "summary_data.csv")

