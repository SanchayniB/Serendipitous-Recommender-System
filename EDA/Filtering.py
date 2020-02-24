
import pandas as pd
from datetime import datetime

def train_filtering(train_loc, years):

    train_data = pd.read_csv(train_loc)

    print('Processing timestamps..........')

    train_data['timestamp'] = train_data['timestamp'].apply(lambda x: datetime.fromtimestamp(x/1000))
    train_data['year'] = train_data['timestamp'].apply(lambda x: x.year)

    print('Done processing timestamps..........')
    train_filtered = train_data[train_data.year.isin(years)]

    print('Done filtering............')
    return(train_filtered)