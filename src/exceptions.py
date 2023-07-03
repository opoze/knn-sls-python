class ModelNotFountException(Exception):
    def __init__(self, file_name="", bucket_name=""):
        self.message = f"Model {file_name} not fount in S3 {bucket_name} bucket."
        super().__init__(self.message)


class StorePredictionException(Exception):
    def __init__(
        self,
        vital_signs: list=[],
        subject_id="",
        predicted_data="",
        error = ""
    ):
        my_dict = {
            "subject_id": subject_id,
            "vital_signs": str(vital_signs),
            "label": predicted_data
        }

        self.message = (
            f"Can not store prediction "
            f"{my_dict}. "
            f"{error}"
        )
        super().__init__(self.message)
        
        
