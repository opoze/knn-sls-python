import json

from .logger import logger
from .predict_application import PredictApplication as Application

class SQSRecordHandler:
    def __init__(self, sqs_record = None):
        self.sqs_record = sqs_record

    def process_record(self):
        try:
            logger.info(f"Processing record {self.sqs_record['messageId']}")
            app = Application()
            jsonBody = self.sqs_record['body']
            body = json.loads(jsonBody)
            payload = body['Message']
            app.run(payload)
            logger.info("Record processed successfully")
        except Exception as error:
            logger.error(f"Error processing record, {error}")
