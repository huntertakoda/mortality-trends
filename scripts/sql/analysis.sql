select *
from clean_mortality_data cmd 
;

# count by location 

select location,
count(*) as location_count
from clean_mortality_data cmd 
group by location 
;

# infant death row = true (count)

select (count(*)) as `Infant Death Flag` 
from clean_mortality_data cmd 
where `Infant Death Flag` = 1
;

# infant death row = false (count)

select (count(*)) as `Infant Death Flag` 
from clean_mortality_data cmd 
where `Infant Death Flag` = 0
;

# orig. age counts by group

select 
	sum(case when age >= 0 then 1 else 0 end) as full_count,
	sum(case when age > 10 then 1 else 0 end) as age_above_10,
	sum(case when age > 20 then 1 else 0 end) as age_above_20,
	sum(case when age > 30 then 1 else 0 end) as age_above_30,
	sum(case when age > 40 then 1 else 0 end) as age_above_40,
	sum(case when age > 50 then 1 else 0 end) as age_above_50,
	sum(case when age > 60 then 1 else 0 end) as age_above_60,
	sum(case when age > 70 then 1 else 0 end) as age_above_70,
	sum(case when age > 80 then 1 else 0 end) as age_above_80
from clean_mortality_data cmd 
;

# age counts by group

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
	count(*) as count_in_bucket
from clean_mortality_data cmd
group by age_bucket
order by age_bucket
;

# summary stats

select 
    count(*) as total_rows,
    avg(age) as average_age,
    avg(`co-morbidity count`) as average_co_morbidity_count,
    avg(`socioeconomic index`) as average_socioeconomic_index
from clean_mortality_data cmd
;

# total deaths per gender

select 
    gender,
    count(*) as total_deaths
from clean_mortality_data cmd
group by gender
order by total_deaths desc
;

# death trends by month

select 
    year,
    month,
    count(*) as deaths_per_month
from clean_mortality_data cmd
group by year, month
order by year, month
;

# top causes of death overall

select 
    `cause of death`,
    count(*) as death_count
from clean_mortality_data cmd
group by `cause of death`
order by death_count desc
limit 10
;

# top causes of death per gender

select 
    gender,
    `cause of death`,
    count(*) as death_count
from clean_mortality_data cmd
group by gender, `cause of death`
order by gender, death_count desc
;

# avg co-moribity / socieconomic index per age group

select 
    `age group`,
    round(avg(`co-morbidity count`), 2) as avg_co_morbid,
    round(avg(`socioeconomic index`), 2) as avg_socioeconomic_index
from clean_mortality_data cmd
group by `age group`
order by `age group`
;

# relationships between numerical columns

select 
    round(avg(age * `co-morbidity count`), 2) as age_co_morbid_interaction,
    round(avg(age * `socioeconomic index`), 2) as age_socioeconomic_interaction,
    round(avg(`co-morbidity count` * `socioeconomic index`), 2) as co_morbid_socioeconomic_interaction
from clean_mortality_data cmd
;





