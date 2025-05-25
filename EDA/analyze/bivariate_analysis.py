from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class bivariateDataAnalysis(ABC):
    @abstractmethod
    def analyze(self, df, feature1, feature2, y=None):
        pass

class NumericNumericAnalysis(bivariateDataAnalysis):
    def analyze(self, df, feature1, feature2, y=None):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} Vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

class CategoricalNumericAnalysis(bivariateDataAnalysis):
    def analyze(self, df, feature1, feature2, y=None):
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()

class SingleVariableScatter(bivariateDataAnalysis):
    def analyze(self, df, feature1, feature2, y=None):
        plt.figure(figsize=(10, 6))
        x1 = df[df[y]==0][feature1]
        x2 = df[df[y]==1][feature1]

        y1 = df[df[y]==0][feature2]
        y2 = df[df[y]==1][feature2]

        plt.scatter(x1, y1, color='blue', label='0')
        plt.scatter(x2, y2, color='red', label='1')

        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.legend()
        plt.title(f'{feature1} Vs {feature2}')
        plt.show()


class BivariateAnalyzer():
    def execute_strategy(self, df, feature1, feature2):
        if feature1 not in df.columns:
            print(f"'{feature1}' is not a valid column in the DataFrame.")
            return
        
        if feature2 not in df.columns:
            print(f"'{feature2}' is not a valid column in the DataFrame.")
            return
        
        dtype1 = df[feature1].dtype
        dtype2 = df[feature2].dtype

        if dtype1 != 'O' and dtype2 != 'O':
            print(f"'{feature1}' and '{feature2}' are a numerical feature.")
            NumericNumericAnalysis().analyze(df, feature1, feature2)

        if dtype1 != 'O' and dtype2 == 'O':
            print(f"'{feature1} is a numerical feature and '{feature2} is a categorical feature")
            CategoricalNumericAnalysis().analyze(df, feature2, feature1)

        if dtype2 != 'O' and dtype1 == 'O':
            print(f"'{feature1} is a numerical feature and '{feature2} is a categorical feature")
            CategoricalNumericAnalysis().analyze(df, feature1, feature2)

        if dtype1 == 'O' and dtype2 == 'O':
            print(f"'{feature1}' and '{feature2}' are a categorical feature.")

    def execute_bivariate_scatter(self, df, feature1, feature2, y):
        SingleVariableScatter().analyze(df, feature1,feature2, y)

if __name__ == "__main__":
    pass