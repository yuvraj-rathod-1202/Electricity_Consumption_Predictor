from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler

class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(self, df):
        pass
    def inverse_transformation(self, df):
        pass

class LogTransformation(FeatureEngineeringStrategy):
    def __init__(self, feature):
        self._feature = feature

    def apply_transformation(self, df):
        df_transformed = df.copy()
        for feature in self._feature:
            df_transformed[feature] = np.log1p(
                df[feature]
            )
        return df_transformed

    def inverse_transformation(self, df):
        df_inversed = df.copy()
        for feature in self._feature:
            df_inversed[feature] = np.expm1(df[feature])
        return df_inversed

class StandardScalling(FeatureEngineeringStrategy):
    def __init__(self, feature):
        self._feature = feature
        self.scaler = StandardScaler()

    def apply_transformation(self, df):
        df_transform = df.copy()
        df_transform[self._feature] = self.scaler.fit_transform(df[[self._feature]])
        return df_transform
    
    def inverse_transformation(self, df):
        df_inverse = df.copy()
        df_inverse[self._feature] = self.scaler.inverse_transform(df[[self._feature]])
        return df_inverse
    
class MinMaxScalling(FeatureEngineeringStrategy):
    def __init__(self, feature):
        self._feature = feature
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def apply_transformation(self, df):
        df_transform = df.copy()
        df_transform[self._feature] = self.scaler.fit_transform(df[[self._feature]])
        df_transform

    def inverse_transformation(self, df):
        df_inverse = df.copy()
        df_inverse[self._feature] = self.scaler.inverse_transform(df[[self._feature]])
        return df_inverse

from sklearn.preprocessing import LabelEncoder

class LabelEncoding(FeatureEngineeringStrategy):
    def __init__(self, feature):
        self._feature = feature
        self.encoder = LabelEncoder()

    def apply_transformation(self, df):
        df_transform = df.copy()
        df_transform[self._feature] = self.encoder.fit_transform(df[self._feature])
        return df_transform

    def inverse_transformation(self, df):
        df_inverse = df.copy()
        df_inverse[self._feature] = self.encoder.inverse_transform(df[self._feature])
        return df_inverse

    

class FeatureEngineer():
    def __init__(self):
        self.transformers = {}

    def execute_transformation(self, df, feature, type):
        if type not in self.transformers:
            if type == "StandardScalling":
                self.transformers[type] = StandardScalling(feature)
            elif type == "MinMaxScalling":
                self.transformers[type] = MinMaxScalling(feature)
            elif type == "LabelEncoding":
                self.transformers[type] = LabelEncoding(feature)
            elif type == "LogTransformation":
                self.transformers[type] = LogTransformation(feature)
            else:
                raise ValueError(f"Unknown transformation type: {type}")

        return self.transformers[type].apply_transformation(df)

    def inverse_transformation(self, df, type):
        if type not in self.transformers:
            raise ValueError(f"No transformer found for type '{type}'. You must apply transformation first.")
        return self.transformers[type].inverse_transformation(df)


if __name__ == "__main__":
    pass