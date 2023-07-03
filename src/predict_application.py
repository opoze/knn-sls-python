from .logger import logger
from .s3_model_repository import S3ModelLoader
from .model import Model
from .dynamo_predictions_repository import DynamoPredictionsRepository

class PredictApplication:
    def __init__(self):
        self.application_name = "KKN classifier"

    def load_model(self):
        logger.info("Loading model from s3")
        file_name = 'knn_serialized_model'
        logger.info(f"Loading {file_name} file from s3")
        knn = S3ModelLoader().get_model(file_name)
        model = Model()
        model.set_model(knn)
        logger.info("S3 model loaded with success")
        return model

    def save_prediction(self, vital_signs: list, subject_id: str, predicted_data: str):
        logger.info("Saving predicted data in dynamoDB")
        predictionRepository = DynamoPredictionsRepository()
        predictionRepository.put_item(subject_id, vital_signs, predicted_data)
        logger.info("Predicted data saved with success")

    def run(self, payload: dict):
        try:
            logger.info(f"Running {self.application_name} with {str(payload)}")
            subject_id = payload['subject_id']
            vital_signs = payload['vital_signs']
            model = self.load_model()
            prediction = model.predict(vital_signs)[0]
            self.save_prediction(vital_signs, subject_id, str(prediction))
            logger.info(f"Application {self.application_name} run with success")
        except Exception as error:
            logger.error(f"Error running application: {error}")
        