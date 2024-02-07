import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
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

    
    fhv_dtypes = {
        'dispatching_base_num': pd.StringDtype(),
        'Affilation_bas_number': pd.StringDtype(),
        'SR_Flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
    }
    parse_dates=['tpep_pickup_datetime','tpep_dropoff_datetime']
    
    def upload(year,type):
        final_data=pd.DataFrame()
        for i in range(1,13):
            
            if i <= 9:
                url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{type}/{type}_tripdata_{year}-0{i}.csv.gz'
            else:
                url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{type}/{type}_tripdata_{year}-{i}.csv.gz'
            print(url)
            if type!='fhv':
                df= pd.read_csv(url, sep=',',compression="gzip",dtype=taxi_dtypes,parse_dates=parse_dates)
                final_data=pd.concat([final_data,df],ignore_index=True)
            else:
                df= pd.read_csv(url, sep=',',compression="gzip",dtype=fhv_dtypes,parse_dates=parse_dates)
                final_data=pd.concat([final_data,df],ignore_index=True)
                    
        return final_data

    # for uploading green_taxi_2019 & 2020 data
    # green_2019=upload(2019,'green')
    # green_2020=upload(2020,'green')
    # merged_green=pd.concat([green_2019,green_2020],ignore_index=True)
    # return merged_green
    
    # for uploading yellow_taxi_2019 & 2020 data
    # yellow_2019=upload(2019,'yellow')
    # yellow_2020=upload(2020,'yellow')
    # merged_yellow=pd.concat([yellow_2019,yellow_2020],ignore_index=True)
    # return merged_yellow
    
    # for uploading fhv_2019 data
    # fhv_2019=upload(2019,'fhv')
    # return fhv_2019

    return upload(2019,'fhv')
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


