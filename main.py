from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.TextSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from src.TextSummarizer.logging import logger

STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<</n/nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<</n/nx==============x")
except Exception as e:
    logger.exception(e)
    raise e