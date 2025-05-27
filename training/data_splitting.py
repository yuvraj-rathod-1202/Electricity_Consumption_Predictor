from abc import ABC, abstractmethod

import pandas as pd
from sklearn.model_selection import train_test_split

class DataSplittingStrategy(ABC):
    @abstractmethod
    def split_data(self, df: pd.DataFrame, target_column: str):
        pass

class SimpleTrainTestSplit(DataSplittingStrategy):
    def __init__(self, test_size=0.2, random_state=42):
        self.test_size = test_size
        self.random_state = random_state

    def split_data(self, df, target_column):
        X = df.drop(columns=target_column)
        y = df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state, shuffle=True
        )

        return X, y, X_train, X_test, y_train, y_test
    
class DataSplitter():
    def split(self, df, target_column, type):
        if type == "simple":
            return SimpleTrainTestSplit().split_data(df, target_column)