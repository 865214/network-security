from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataTransformationConfig, DataValidationConfig
from networksecurity.components.data_validation import DataValidation
import sys

if __name__ == "__main__":
    try:
        trainingpiprlineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpiprlineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpiprlineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed") 
        print(data_validation_artifact) 
        data_transformation_config = DataTransformationConfig(trainingpiprlineconfig)
        logging.info('Data Transformation Started')
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transsformation_artifact = data_transformation.initiate_data_transformation()
        logging.info('Data Transformation Completed')
        print(data_transsformation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
        