	
import sys
from .logger import logger
from .sqs_record_handler import SQSRecordHandler

# Add vendor folder to sys path
sys.path.insert(0, 'src/vendor') 

def handler(event, context):
    logger.info("Serverless function called")
    try:
        logger.info(f"Processing {len(event['Records'])} records")
        for record in event['Records']:
            sqsRecordHandler = SQSRecordHandler(record)
            sqsRecordHandler.process_record()
    except Exception as error:
        logger.error(f"Serverless function error, {error}")

    return "Done"