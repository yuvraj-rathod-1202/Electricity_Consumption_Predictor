import pandas as pd

class TypeConvert():
    def convert(self, df, feature, to):
        if to == "numeric":
            df[feature] = df[feature].apply(pd.to_numeric, errors="coerce")
        elif to == "datetime":
            df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], errors="coerce")
            df.drop(columns=["Date", "Time"], inplace=True)
        return df