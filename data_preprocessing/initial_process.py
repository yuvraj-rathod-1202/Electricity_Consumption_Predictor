from type_convert import TypeConvert

import pandas as pd

class InitialProcess():
    def process(slef, df):
        numeric_cols = [
            'Global_active_power',
            'Global_reactive_power',
            'Voltage',
            'Global_intensity',
            'Sub_metering_1',
            'Sub_metering_2',
        ]

        convert = TypeConvert()
        df = convert.convert(df, numeric_cols, "numeric")
        df = convert.convert(df, ['Date'], "datetime")

        df['Datetime'] = df['Datetime'].dt.floor('H')

        agg_sum = df.groupby('Datetime')[[
            'Global_active_power', 
            'Global_reactive_power', 
            'Global_intensity', 
            'Sub_metering_1', 
            'Sub_metering_2', 
            'Sub_metering_3'
        ]].sum().reset_index()

        agg_mean = df.groupby('Datetime')[['Voltage']].mean().reset_index()

        df = pd.merge(agg_sum, agg_mean, on='Datetime')
        df.drop(columns=['Global_intensity'], inplace=True)
        return df