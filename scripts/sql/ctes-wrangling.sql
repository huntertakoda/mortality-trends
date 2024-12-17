with 
# cte 1: calculate age buckets and total deaths
age_bucket_counts as (
    select 
        case 
            when age >= 70 then '70-80'
            when age >= 60 then '60-70'
            when age >= 50 then '50-60'
            when age >= 40 then '40-50'
            when age >= 30 then '30-40'
            when age >= 20 then '20-30'
            when age >= 10 then '10-20'
            when age >= 0 then '0-10'
            else '80+'
        end as age_bucket,
        count(*) as total_deaths
    from clean_mortality_data
    group by age_bucket
),

# cte 2: gender-specific stats for age buckets
gender_age_bucket_stats as (
    select 
        gender,
        case 
            when age >= 70 then '70-80'
            when age >= 60 then '60-70'
            when age >= 50 then '50-60'
            when age >= 40 then '40-50'
            when age >= 30 then '30-40'
            when age >= 20 then '20-30'
            when age >= 10 then '10-20'
            when age >= 0 then '0-10'
            else '80+'
        end as age_bucket,
        count(*) as deaths,
        round(avg(`co-morbidity count`), 2) as avg_co_morbidity,
        round(avg(`socioeconomic index`), 2) as avg_socioeconomic
    from clean_mortality_data
    group by gender, age_bucket
),

# cte 3: monthly deaths by location and gender
monthly_gender_location_trends as (
    select 
        year,
        month,
        location,
        gender,
        count(*) as total_deaths
    from clean_mortality_data
    group by year, month, location, gender
    order by year, month, location
),

# cte 4: top causes of death by gender and age group
gender_age_top_causes as (
    select 
        gender,
        `age group`,
        `cause of death`,
        count(*) as total_deaths
    from clean_mortality_data
    group by gender, `age group`, `cause of death`
    order by gender, `age group`, total_deaths desc
),

# cte 5: high-risk socioeconomic stats by gender
high_risk_gender_stats as (
    select 
        gender,
        round(avg(`socioeconomic index`), 2) as avg_socioeconomic_index,
        round(max(`co-morbidity count`), 2) as max_co_morbidity
    from clean_mortality_data
    where `socioeconomic index` < 30
    group by gender
),

# cte 6: create a combined gender and location mortality overview
gender_location_overview as (
    select 
        gender,
        location,
        count(*) as total_deaths,
        round(avg(`co-morbidity count`), 2) as avg_co_morbidity
    from clean_mortality_data
    group by gender, location
),

# final cte 1: gender-specific high-risk locations
high_risk_locations as (
    select 
        g.gender,
        g.location,
        g.total_deaths,
        h.avg_socioeconomic_index
    from gender_location_overview g
    join high_risk_gender_stats h on g.gender = h.gender
    where g.total_deaths > 500
),

# final cte 2: consolidated mortality insights
mortality_insights as (
    select 
        g.gender,
        a.age_bucket,
        g.deaths,
        g.avg_co_morbidity,
        g.avg_socioeconomic
    from gender_age_bucket_stats g
    join age_bucket_counts a on g.age_bucket = a.age_bucket
    where g.deaths > 100
)
# final select statements
select 
    'high-risk locations' as analysis_type, 
    gender, 
    location, 
    total_deaths, 
    avg_socioeconomic_index
from high_risk_locations

union all

select 
    'consolidated mortality insights' as analysis_type, 
    gender, 
    age_bucket, 
    deaths, 
    avg_co_morbidity
from mortality_insights
;
