# warehouse table, age bucket counts

create table age_bucket_summary as
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
;

select *
from age_bucket_summary abs2 
;

# warehouse table, top causes of death by year

create table top_causes_by_year as
select 
    year,
    `cause of death`,
    count(*) as death_count
from clean_mortality_data
group by year, `cause of death`
order by year, death_count desc
;

select *
from top_causes_by_year tcby 
;

# warehouse table, gender and age group mortality

create table gender_age_group_summary as
select 
    gender,
    `age group`,
    count(*) as total_deaths,
    round(avg(`co-morbidity count`), 2) as avg_co_morbidity,
    round(avg(`socioeconomic index`), 2) as avg_socioeconomic
from clean_mortality_data
group by gender, `age group`
;

select *
from gender_age_group_summary gags 
;

# warehouse table, monthly death trends

create table monthly_death_trends as
select 
    year,
    month,
    count(*) as deaths_per_month
from clean_mortality_data
group by year, month
order by year, month
;

select *
from monthly_death_trends mdt 
;

# warehouse table, gender-specific top causes

create table gender_top_causes as
select 
    gender,
    `cause of death`,
    count(*) as total_deaths
from clean_mortality_data
group by gender, `cause of death`
order by gender, total_deaths desc
;

select *
from gender_top_causes gtc 
;

# warehouse table, socioeconomic and co-morbidity stats by gender

create table gender_socioeconomic_stats as
select 
    gender,
    round(avg(`co-morbidity count`), 2) as avg_co_morbidity,
    round(avg(`socioeconomic index`), 2) as avg_socioeconomic_index
from clean_mortality_data
group by gender
;

select *
from gender_socioeconomic_stats gss 
;
