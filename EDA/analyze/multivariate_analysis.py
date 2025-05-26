from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class MultivariateAnalysis(ABC):
    def analyze(self, df):
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)

    @abstractmethod
    def generate_correlation_heatmap(self, df):
        pass

    @abstractmethod
    def generate_pairplot(self, df):
        pass

class SimpleMultivariateAnalysis(MultivariateAnalysis):
    def generate_correlation_heatmap(self, df):
        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

    def generate_pairplot(self, df):
        sns.pairplot(df)
        plt.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()


if __name__ == "__main__":
    pass