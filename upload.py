import pandas as pd


taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': pd.Int64Dtype(),
        'extra': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float,
}

parse_dates=['tpep_pickup_datetime','tpep_dropoff_datetime']
final_data= pd.DataFrame()

def upload(year,type):
    for i in range(1,13):
        
        if i <= 9:
            url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{type}/{type}_tripdata_{year}-0{i}.csv.gz'
        else:
            url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{type}/{type}_tripdata_{year}-{i}.csv.gz'
        print(url)
        df= pd.read_csv(url, sep=',',compression="gzip",dtype=taxi_dtypes,parse_dates=parse_dates)
        final_data=pd.concat([final_data,df],ignore_index=True)
    return final_data

# green_2019=upload(2019,'green')
# green_2020=upload(2020,'green')
# merged_green=pd.concat([green_2019,green_2020],ignore_index=True)

# yellow_2019=upload(2019,'yellow')
# yellow_2020=upload(2020,'yellow')
# merged_green=pd.concat([yellow_2019,yellow_2020],ignore_index=True)

fhv_2019=upload(2019,'fhv')


