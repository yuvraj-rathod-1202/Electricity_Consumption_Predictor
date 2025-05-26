from extract_ingest.ingest import Ingestor
from data_preprocessing.initial_process import InitialProcess
from data_preprocessing.missing_value_handling import MissingValueHandler, FillMissingValue, DropMissingValue
from data_preprocessing.feature_engineering import FeatureEngineer
from data_preprocessing.outliers_detection import OutlierProcessing

class TrainingPipeline():
    def training_pipeline(self):

        data = Ingestor().ingest("C:\projects\ml_learn\End-To-End-Projects\Electricity_Consumption_Predictor\extracted_data\household_power_consumption.txt")

        data = InitialProcess().process(data)

        filled_data = MissingValueHandler(FillMissingValue()).handle_missing_values(data)

        featured_data = FeatureEngineer().execute_transformation(filled_data, ['Global_active_power', 'Global_reactive_power', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'], "LogTransformation")
        featured_data = FeatureEngineer().execute_transformation(featured_data, 'Voltage', "StandardScalling")

        cleaned_data = OutlierProcessing().process_outliers(featured_data, featured_data.columns, "IQROutlierDetection")

        return cleaned_data
    
if __name__ == "__main__":
    pass
        