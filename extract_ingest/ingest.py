from abc import ABC, abstractmethod
import os
import pandas as pd

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, filePath: str):
        pass

class DataFrameIngest(DataIngestor):
    def ingest(self, filePath):
        extension = os.path.splitext(filePath)[1].lower()
        if extension != ".csv":
            raise ValueError("File is not a valid CSV type")
        
        df = pd.read_csv(filePath)
        return df

class Ingestor:
    def ingest(self, filePath):
        return DataFrameIngest().ingest(filePath)

if __name__ == "__main__":
    # ingestor = Ingestor()
    # csv_path = "path/to/your/file.csv"
    # if os.path.exists(csv_path):
    #     df = ingestor.ingest(csv_path)
    #     print(df.head())
    # else:
    #     print(f"File not found: {csv_path}")
    pass
