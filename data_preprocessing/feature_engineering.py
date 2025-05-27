from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler

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
    
    def inverse_transformation(self, df):
        df_inverse = df.copy()
        encoded_columns = self.encoder.get_feature_names_out([self._feature])
        encoded_data = df[encoded_columns]
        original_feature = self.encoder.inverse_transform(encoded_data)
        df_inverse[self._feature] = original_feature
        df_inverse = df_inverse.drop(columns=encoded_columns)
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
            elif type == "OneHotEncodding":
                self.transformers[type] = OneHotEncodding(feature)
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