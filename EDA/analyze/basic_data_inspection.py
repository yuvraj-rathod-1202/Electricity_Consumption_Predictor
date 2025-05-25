from abc import ABC, abstractmethod

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df):
        pass

class DataTypeInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df):
        print("\nData type and not null count")
        print(df.info())


class DataSummaryInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df):
        try:
            print("\nData Summary (Numeric Feature)")
            print(df.describe())
            print("\nData Summary (Categorical Feature)")
            print(df.describe(include=["O"]))
        except:
            print("some error")


class DataInspector():
    def __init__(self, strategy):
        self._strategy = strategy

    def setStrategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, df):
        self._strategy.inspect(df)

if __name__ == "__main__":
    pass