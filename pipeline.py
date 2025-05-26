from extract_ingest.ingest import Ingestor
from data_preprocessing.initial_process import InitialProcess
from data_preprocessing.missing_value_handling import MissingValueHandler, FillMissingValue, DropMissingValue

class TrainingPipeline():
    def training_pipeline(self):

        data = Ingestor().ingest("C:\projects\ml_learn\End-To-End-Projects\Electricity_Consumption_Predictor\extracted_data\household_power_consumption.txt")

        data = InitialProcess().process(data)

        filled_data = MissingValueHandler(FillMissingValue()).handle_missing_values(data)
        