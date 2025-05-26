from extract_ingest.ingest import Ingestor
from data_preprocessing.initial_process import InitialProcess

class TrainingPipeline():
    def training_pipeline(self):

        data = Ingestor().ingest("C:\projects\ml_learn\End-To-End-Projects\Electricity_Consumption_Predictor\extracted_data\household_power_consumption.txt")

        data = InitialProcess().process(data)