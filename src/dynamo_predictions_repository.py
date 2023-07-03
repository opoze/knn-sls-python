import boto3
import json

from .exceptions import StorePredictionException

class DynamoPredictionsRepository :
    def __init__(self, table_name: str = 'predictions'):
        self.table_name = table_name
        self.client = boto3.client('dynamodb', endpoint_url='http://localhost:4566')


    def put_item(
            self,
            subject_id: str = '1',
            vital_signs: list = [],
            label: str = '1'
        ):
        try:
            self.client.put_item(
                TableName=self.table_name,
                Item = {
                    'subject_id': {
                        'N': subject_id
                    },
                    'vital_sign': {
                        'S':  json.dumps(vital_signs)
                    },
                    'label': {
                        'N': label
                    }
                }
            )
        except Exception as error:
            raise StorePredictionException(vital_signs, subject_id, label, error)

    def list_tables(self):
        return self.client.list_tables()
