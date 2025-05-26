from abc import ABC, abstractmethod

class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df):
        pass

class DropMissingValue(MissingValueHandlingStrategy):
    def __init__(self, axis=0, thresh=None):
        self.axis = axis
        self.thresh = thresh

    def handle(self, df):
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        return df_cleaned
    
class FillMissingValue(MissingValueHandlingStrategy):
    def __init__(self, method="mean", fill_value=None):
        self.method = method
        self.fill_value = fill_value

    def handle(self, df):
        df_cleaned = df.copy()
        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(
                df[numeric_columns].mean()
            )
        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(
                df[numeric_columns].median()
            )
        elif self.method == "mode":
            for column in df_cleaned.columns:
                df_cleaned[column].fillna(df[column].mode().iloc[0], inplace=True)
        elif self.method == "constant":
            df_cleaned = df_cleaned.fillna(self.fill_value)
        else:
            print(f"Unknown method '{self.method}'. No missing values handled.")

        return df_cleaned
    
class MissingValueHandler():
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def handle_missing_values(self, df):
        return self._strategy.handle(df)
    
if __name__ == "__main__":
    pass