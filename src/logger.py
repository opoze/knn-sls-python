import logging
import boto3
from botocore.exceptions import NoCredentialsError


class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_format = "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s"
        formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

class LocalStackCloudWatchHandler(logging.Handler):
    def __init__(self, log_group, log_stream):
        super().__init__()
        self.log_group = log_group
        self.log_stream = log_stream
        self.client = boto3.client('logs', endpoint_url='http://localhost:4566')

    def emit(self, record):
        log_entry = self.format(record)

        try:
            self.client.put_log_events(
                logGroupName=self.log_group,
                logStreamName=self.log_stream,
                logEvents=[
                    {
                        'timestamp': int(record.created * 1000),
                        'message': log_entry
                    }
                ]
            )
        except NoCredentialsError:
            print("No AWS credentials found. Please configure your credentials.")

class LoggerHandler():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.loggerHandler = LocalStackCloudWatchHandler(
            log_group='/aws/lambda/predict-function',
            log_stream='log-stream'
        )
        self.formatter = CustomFormatter()
        self.loggerHandler.setFormatter(self.formatter)
        self.logger.addHandler(self.loggerHandler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

logger = LoggerHandler()