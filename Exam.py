import pandas as pd
file_path = 'D:/AQI_Data.csv'
data = pd.read_csv(file_path)

if 'City' in data.columns and 'AQI' in data.columns and 'PM10' in data.columns:
    grouped_data = data.groupby('City').agg({
        'AQI': 'mean',      
        'PM10': 'max'       
    }).reset_index()

    grouped_data.rename(columns={'AQI': 'Average AQI', 'PM10': 'Maximum PM10'}, inplace=True)

    print(grouped_data)
else:
    print("The required columns ('City', 'AQI', 'PM10') are not present in the data.")




# group the data by city and calculate the following for each city
# a) Average AQI
# b) Maximum PM10 level