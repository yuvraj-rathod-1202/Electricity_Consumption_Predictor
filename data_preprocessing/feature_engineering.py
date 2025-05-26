from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler

class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(self, df):
        pass


class StandardScalling(FeatureEngineeringStrategy):
    def __init__(self, feature):
        self._feature = feature
        self.scaler = StandardScaler()

    def apply_transformation(self, df):
        df_transform = df.copy()
        df_transform[self._feature] = self.scaler.fit_transform(df[[self._feature]])
        return df_transform
    
class MinMaxScalling(FeatureEngineeringStrategy):
    def __init__(self, feature):
        self._feature = feature
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def apply_transformation(self, df):
        df_transform = df.copy()
        df_transform[self._feature] = self.scaler.fit_transform(df[[self._feature]])
        df_transform

class OneHotEncodding(FeatureEngineeringStrategy):
    def __init__(self, feature):
        self._feature = feature
        self.encoder = OneHotEncoder(drop="first", sparse_output=False)

    def apply_transformation(self, df):
        df_transform = df.copy()
        encoded_df = pd.DataFrame(
            self.encoder.fit_transform(df[[self._feature]]),
            columns=self.encoder.get_feature_names_out([self._feature]),
            index=df.index
        )
        df_transform = df_transform.drop(columns=self._feature)
        df_transform = pd.concat([df_transform, encoded_df], axis=1)
        return df_transform
    

class FeatureEngineer():
    def execute_transformation(self, df, feature, type):
        if type=="StandardScalling":
            return StandardScalling(feature).apply_transformation(df)
        elif type=="MinMaxScalling":
            return MinMaxScalling(feature).apply_transformation(df)
        elif type=="OneHotEncodding":
            return OneHotEncodding(feature).apply_transformation(df)

if __name__ == "__main__":
    pass