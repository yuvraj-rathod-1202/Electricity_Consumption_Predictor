from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class MissingValueAnalysis(ABC):
    def analyze(self, df):
        self.MissingValueIdentify(df)
        self.MissingValueAnalysis(df)

    def MissingValueIdentify(self, df):
        pass

    def MissingValueAnalysis(self, df):
        pass


class SimpleMisssingValueAnalysis(MissingValueAnalysis):
    def MissingValueIdentify(self, df):
        print("\nMissing Value count by Column")
        missing_val = df.isnull().sum()
        print(missing_val[missing_val > 0])

    def MissingValueAnalysis(self, df):
        print("\n Visualizing Missing Value")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title("Missing Value Analysis")
        plt.show()


if __name__ == "__main__":
    pass