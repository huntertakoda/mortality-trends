library(readr)      
library(dplyr)
library(ggplot2)
library(corrplot)
library(ROSE)
library(caret)
library(e1071)
library(zoo)

# importing

mortality_data <- read_csv("clean_mortality_data.csv")

# clean column names: replace spaces, hyphens, and special characters with underscores
colnames(mortality_data) <- gsub(" ", "_", colnames(mortality_data))
colnames(mortality_data) <- gsub("-", "_", colnames(mortality_data))
colnames(mortality_data) <- gsub("/", "_", colnames(mortality_data))

# check for missing data

print(colSums(is.na(mortality_data)))

# filter data by gender and calculate correlation matrices

male_data <- mortality_data %>% filter(Gender == "Male") %>% select(Age, Co_morbidity_Count, Socioeconomic_Index)
female_data <- mortality_data %>% filter(Gender == "Female") %>% select(Age, Co_morbidity_Count, Socioeconomic_Index)

male_cor <- cor(male_data)
female_cor <- cor(female_data)

# plot correlation matrices

par(mfrow = c(1, 2))
corrplot(male_cor, method = "color", type = "upper", tl.col = "black", title = "Male Correlations", mar = c(0,0,1,0))
corrplot(female_cor, method = "color", type = "upper", tl.col = "black", title = "Female Correlations", mar = c(0,0,1,0))
par(mfrow = c(1, 1))

# t-test for socioeconomic index by gender

t_test_result <- t.test(Socioeconomic_Index ~ Gender, data = mortality_data)
print(t_test_result)

# anova for co-morbidity count by age group

anova_result <- aov(Co_morbidity_Count ~ Age_Group, data = mortality_data)
summary(anova_result)

# linear regression model

lm_model <- lm(Co_morbidity_Count ~ Age + Socioeconomic_Index + Gender, data = mortality_data)
summary(lm_model)

mortality_data_numeric <- mortality_data %>%
  select(Infant_Death_Flag, Age, Co_morbidity_Count, Socioeconomic_Index, Gender)

# convert 'Gender' to factor

mortality_data_numeric <- mortality_data_numeric %>%
  mutate(Gender = as.factor(Gender))

# apply ROSE to balance data

balanced_data <- ROSE(Infant_Death_Flag ~ ., data = mortality_data_numeric, seed = 123)$data

# logistic regression model on balanced data

logistic_model_fixed <- glm(Infant_Death_Flag ~ Age + Socioeconomic_Index + Gender, 
                            data = balanced_data, family = binomial)
summary(logistic_model_fixed)

# predicted probabilities

balanced_data$pred <- predict(logistic_model_fixed, type = "response")

# plot predicted probabilities

ggplot(balanced_data, aes(x = pred, fill = as.factor(Infant_Death_Flag))) +
  geom_histogram(position = "identity", alpha = 0.6, bins = 30) +
  labs(title = "Predicted Probabilities of Infant Death", x = "Predicted Probability", 
       fill = "Infant Death Flag")

# advanced linear regression with interaction terms

lm_model_interaction <- lm(Co_morbidity_Count ~ Age * Socioeconomic_Index + Gender, 
                           data = mortality_data)
summary(lm_model_interaction)

plot(lm_model_interaction)

# hierarchical correlation heatmap

cor_matrix_full <- cor(mortality_data %>% 
                         select(Age, Co_morbidity_Count, Socioeconomic_Index))

# plot

corrplot(cor_matrix_full, 
         method = "color", 
         type = "upper", 
         order = "hclust", 
         addrect = 2, 
         title = "Hierarchical Correlation Heatmap", 
         mar = c(0, 0, 2, 0))

# time-series decomposition for deaths over time

time_series <- mortality_data %>%
  group_by(Year, Month) %>%
  summarise(total_deaths = n(), .groups = "drop") %>%
  mutate(date = as.Date(paste(Year, Month, "01", sep = "-")))

ts_data <- ts(time_series$total_deaths, start = c(min(time_series$Year), 1), frequency = 12)
decomp <- decompose(ts_data)
plot(decomp)

# clustering: k-means clustering on co-morbidity and socioeconomic index

clustering_data <- mortality_data %>% select(Co_morbidity_Count, Socioeconomic_Index)
set.seed(123)
kmeans_result <- kmeans(clustering_data, centers = 3, nstart = 10)

mortality_data$Cluster <- as.factor(kmeans_result$cluster)

ggplot(mortality_data, aes(x = Co_morbidity_Count, y = Socioeconomic_Index, color = Cluster)) +
  geom_point(alpha = 0.6) +
  labs(title = "K-means Clustering: Co-morbidity Count vs Socioeconomic Index", 
       x = "Co-morbidity Count", y = "Socioeconomic Index", color = "Cluster")

# enhanced time-series analysis with rolling averages

time_series %>%
  mutate(rolling_avg = zoo::rollmean(total_deaths, k = 3, fill = NA)) %>%
  ggplot(aes(x = date)) +
  geom_line(aes(y = total_deaths), color = "blue", alpha = 0.6) +
  geom_line(aes(y = rolling_avg), color = "red", size = 1) +
  labs(title = "Monthly Mortality Trends with Rolling Average", 
       x = "Time", y = "Total Deaths") +
  theme_minimal()

# save outputs to csv for reporting purposes

write_csv(mortality_data, "enhanced_mortality_data.csv")
write_csv(time_series, "time_series_analysis.csv")
