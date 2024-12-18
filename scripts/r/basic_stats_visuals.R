library(readr)      
library(dplyr)
library(ggplot2)
library(corrplot)

# importing

mortality_data <- read_csv("clean_mortality_data.csv")

# check structure and first few rows

glimpse(mortality_data)
head(mortality_data)

# check for missing values

sapply(mortality_data, function(x) sum(is.na(x)))

# summary of key stats

summary(mortality_data)

# basic summary stats for numerical columns

mortality_data %>%
  summarise(
    avg_age = mean(Age),
    median_age = median(Age),
    min_age = min(Age),
    max_age = max(Age),
    avg_comorbidity = mean(`Co-morbidity Count`),
    avg_socioeconomic = mean(`Socioeconomic Index`),
    infant_death_rate = mean(`Infant Death Flag`) * 100
  )

# average age, co-morbidity, and socioeconomic index grouped by gender

mortality_data %>%
  group_by(Gender) %>%
  summarise(
    avg_age = mean(Age),
    avg_comorbidity = mean(`Co-morbidity Count`),
    avg_socioeconomic = mean(`Socioeconomic Index`),
    total_deaths = n()
  )

# count deaths for each age group

mortality_data %>%
  group_by(`Age Group`) %>%
  summarise(total_deaths = n()) %>%
  arrange(desc(total_deaths))

# bar chart showing gender distribution

ggplot(mortality_data, aes(x = Gender)) +
  geom_bar(fill = "skyblue") +
  labs(title = "gender distribution", x = "gender", y = "count")

# histogram of age

ggplot(mortality_data, aes(x = Age)) +
  geom_histogram(binwidth = 5, fill = "lightgreen", color = "black") +
  labs(title = "age distribution", x = "age", y = "frequency")

# boxplot of socioeconomic index for each gender

ggplot(mortality_data, aes(x = Gender, y = `Socioeconomic Index`, fill = Gender)) +
  geom_boxplot() +
  labs(title = "socioeconomic index by gender", x = "gender", y = "socioeconomic index")

# correlation matrix between age, co-morbidity count, and socioeconomic index

numeric_data <- mortality_data %>%
  select(Age, `Co-morbidity Count`, `Socioeconomic Index`)

cor_matrix <- cor(numeric_data)

# plot correlation matrix

corrplot(cor_matrix, method = "color", type = "upper", tl.col = "black", tl.srt = 45)






