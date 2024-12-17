# dynamically calculate age buckets, gender stats, and top causes

select 'age bucket counts' as analysis_type, 
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
       end as bucket,
       count(*) as count_in_bucket
from clean_mortality_data
group by bucket

union all

select 'gender age bucket' as analysis_type,
       concat(gender, ' - ', 
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
       end) as gender_age_bucket,
       count(*) as deaths
from clean_mortality_data
group by gender, gender_age_bucket

union all

select 'top causes' as analysis_type, 
       `cause of death`, 
       count(*) as total_deaths
from clean_mortality_data
group by `cause of death`
order by total_deaths desc
limit 5

union all

select 'gender avg stats' as analysis_type, 
       gender, 
       round(avg(`co-morbidity count`), 2) as avg_co_morbidity
from clean_mortality_data
group by gender
;

select 
    'gender stats' as analysis_type,
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
    round(avg(`co-morbidity count`), 2) as avg_co_morbidity,
    round(avg(`socioeconomic index`), 2) as avg_socioeconomic_index,
    count(*) as total_deaths,
    sum(case when `infant death flag` = 1 then 1 else 0 end) as infant_deaths
from clean_mortality_data
group by gender, age_bucket
order by gender, age_bucket
;

