from abc import ABC, abstractmethod
from zipfile import ZipFile
import os

class DataExtractor(ABC):
    @abstractmethod
    def extract(self, filePath: str):
        pass

class ZipDataExtractor(DataExtractor):
    def extract(self, filePath):
        extension = os.path.splitext(filePath)[1].lower()
        if extension != ".zip":
            raise ValueError("File is not a valid zip type")
        
        with ZipFile(filePath, 'r') as zip_ref:
            zip_ref.printdir()
            output_dir = 'extracted_data'
            os.makedirs(output_dir, exist_ok=True)
            zip_ref.extractall(output_dir)



class ConvertFile():
    def convert(self, filePath):
        extension = os.path.splitext(filePath)[1].lower()
        if extension == ".zip":
            ZipDataExtractor().extract(filePath)
        else:
            raise ValueError(f"Unsupported file type: {extension}")


if __name__ == "__main__":
    convertFile = ConvertFile()
    zip_path = os.path.join('C:\projects\ml_learn\End-To-End-Projects\electricity_prediction\data\individual+household+electric+power+consumption.zip')
    convertFile.convert(zip_path)