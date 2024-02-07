if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    

    print('Rows with zero passengers',data['passenger_count'].isin([0]).sum())    

    #data = data[data['passenger_count'] > 0 or data['trip_distance'] > 0]
    data.columns = (data.columns
                    .str.repalace(' ','_')
                    .str.lower()
                    )
    
    return data
