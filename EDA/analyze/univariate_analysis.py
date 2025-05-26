from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class UnivariateDataAnalysis(ABC):
    @abstractmethod
    def analysis(self, df, feature):
        pass

class NumericDataAnalysis(UnivariateDataAnalysis):
    def analysis(self, df, feature):
        
        plt.figure(figsize=(10, 6))
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f"distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("frequency")
        plt.show()

class CategoricalDataAnalysis(UnivariateDataAnalysis):
    def analysis(self, df, feature):
        
        plt.figure(figsize=(10, 6))
        sns.countplot(x=feature, data=df, palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()


class UnivariateAnalyzer():
    def execute_strategy(self, df, feature):

        if feature not in df.columns:
            print(f"'{feature}' is not a valid column in the DataFrame.")
            return

        dtype = df[feature].dtype

        if dtype != 'O':
            print(f"'{feature}' is a numerical feature.")
            NumericDataAnalysis().analysis(df, feature)
        elif dtype == 'O':
            print(f"'{feature}' is a categorical feature.")
            CategoricalDataAnalysis().analysis(df, feature)
        else:
            print(f"'{feature}' has an unsupported data type: {dtype}")
        

if __name__ == "__main__":
    pass