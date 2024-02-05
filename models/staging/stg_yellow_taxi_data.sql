{{ config(materialized="view") }}

select * from  {{ source('staging','yellow_taxi_data') }} limit 100