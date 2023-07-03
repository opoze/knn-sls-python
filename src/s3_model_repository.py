import boto3
import botocore
import joblib
from io import BytesIO

from .exceptions import ModelNotFountException

class S3ModelLoader:
    def __init__(self):
        self.bucket_name = 'model-bucket'
        self.client = boto3.client('s3', endpoint_url='http://localhost:4566')

    def get_model(self, file_name = 'knn_serialized_model'):
        try:
            with BytesIO() as data:
                self.client.download_fileobj(self.bucket_name, file_name, data)
                data.seek(0)
                return joblib.load(data)
        except botocore.exceptions.ClientError as error:
            httpErrorCode = error.response['Error']['Code']
            if httpErrorCode == "404":
                raise ModelNotFountException(file_name, self.bucket_name)
            else:
                raise error
        except Exception as error:
            raise error