# mortality-trends

# Mortality Analysis and Predictive Modeling

## Overview

this project provides a comprehensive analysis of mortality trends, incorporating **data ingestion**, **statistical analysis**, **machine learning models**, and **interactive visualizations**. the workflow uses a multi-technology approach: **golang**, **sql**, **r**, **python**, and **tableau** to ensure end-to-end processing, analysis, and insights.

---

## tools and technologies

- **golang**: data ingestion, cleaning, preprocessing, and exploratory analysis.  
- **sql**: data wrangling, warehousing, and advanced querying.  
- **r**: statistical analysis, time-series decomposition, and advanced visualizations.  
- **python**: machine learning model development, feature engineering, and evaluation.  
- **tableau**: interactive dashboards for exploratory and visual insights.  

---

## project workflow

1. **data preprocessing and early analysis** (golang)  
2. **data management and warehousing** (sql)  
3. **statistical analysis and visualization** (r)  
4. **machine learning models** (python)  
5. **interactive dashboards** (tableau)  

---

## key features

### section 1: golang - data ingestion and preprocessing

**high-value skills used**:
- efficient csv file reading and parsing  
- dynamic column creation (e.g., "age group")  
- interactive querying for filtering datasets  
- foundational visualizations for gender distribution  

**key outputs**:  
- cleaned dataset: **cleaned_mortality_data.csv**  
- train-test splits: **train_data.csv**, **test_data.csv**  
- monthly mortality trends and top causes of death  
- correlation coefficients for key numeric relationships  

---

### section 2: sql - data warehousing and wrangling

**high-value skills used**:
- dynamic age bucket creation using `case` statements  
- warehouse tables for pre-aggregated, optimized insights  
- advanced querying using **ctes** for complex relationships  
- performance optimization with indexing  

**key outputs**:  
- aggregated tables for age buckets, gender, and cause-specific trends  
- pre-aggregated mortality insights for performance optimization  
- monthly mortality patterns and high-risk socioeconomic trends  

---

### section 3: r - advanced statistical analysis

**high-value skills used**:
- correlation matrices and regression analysis  
- time-series decomposition and rolling averages  
- anova tests for group comparisons  
- visualization-driven insights (scatter plots, boxplots, and heatmaps)  

**key outputs**:  
- time-series trends with decomposition and rolling averages  
- linear regression analysis on predictors of co-morbidity  
- anova insights for age group variations  
- visual outputs: **correlation matrix**, **boxplots**, and **scatter plots**  

---

### section 4: python - machine learning models

**high-value skills used**:  
- feature engineering and selection for model optimization  
- advanced models: **random forest**, **gradient boosting**, and **logistic regression**  
- model evaluation with metrics like accuracy, roc-auc, and f1-score  
- residual analysis and feature importance visualization  

**key outputs**:  
- trained and tuned models with hyperparameter optimization  
- evaluation reports: accuracy, precision, and roc-auc  
- feature importance insights and residual validation  
- saved models and comprehensive summary reports  

---

### section 5: tableau - interactive dashboards

**high-value skills used**:  
- dynamic filters for year, gender, age group, location, and cause of death  
- interactive line charts, bar charts, heatmaps, and scatter plots  
- cohesive dashboard layouts for high-level and deep-dive insights  

**dashboard 1: mortality overview**:  
- mortality trends over time (line chart)  
- top causes of death (bar chart)  
- gender-based mortality distribution (bar chart)  
- age group mortality analysis (bar chart)  

**dashboard 2: mortality deep dive**:  
- location-based mortality heatmap  
- co-morbidity vs socioeconomic index (scatter plot)  
- monthly mortality trends (line chart)  
- cause-specific mortality trends over time (line chart)  

**key outputs**:  
- two polished dashboards enabling high-level and detailed mortality analysis  
- dynamic filters for user-driven exploration of trends, causes, and relationships  

---

## final outputs

- **cleaned and preprocessed dataset**: cleaned_mortality_data.csv  
- **train-test splits**: train_data.csv, test_data.csv  
- **aggregated sql tables**: dynamic age groups, causes, and monthly trends  
- **statistical insights**: correlation matrices, time-series trends, and regression results  
- **machine learning models**: random forest, logistic regression, and gradient boosting  
- **interactive dashboards**:  
  - dashboard 1: mortality overview  
  - dashboard 2: mortality deep dive  

---

## notes

- this project integrates multiple technologies for end-to-end mortality analysis.  
- interactive dashboards and statistical models provide actionable insights.  
- visualizations enhance clarity, enabling exploration of trends and patterns.  
- each section bridges into the next, ensuring a seamless and modular workflow.  
