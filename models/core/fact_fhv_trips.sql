{{
    config(
        materialized='table'
    )
}}

with fhv_tripdata as (
    select *, 
        'FHV' as service_type
    from {{ ref('stg_fhv_taxi_data') }}
), 
dim_zones as (
    select * from {{ ref('dimension_zones') }}
    where borough != 'Unknown'
)
select 
fhv_tripdata.vendorid,	
fhv_tripdata.ratecodeid,		
fhv_tripdata.pickup_locationid,	
fhv_tripdata.dropoff_locationid,	
fhv_tripdata.pickup_datetime,	
fhv_tripdata.dropoff_datetime,	
fhv_tripdata.store_and_fwd_flag

from fhv_tripdata
inner join dim_zones as pickup_zone
on fhv_tripdata.pickup_locationid = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on fhv_tripdata.dropoff_locationid = dropoff_zone.locationid

