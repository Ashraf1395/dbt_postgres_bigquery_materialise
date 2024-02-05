{{ config(materialized="view") }}

select * from  {{ source('stagin','yellow_taxi_data') }} limit 100