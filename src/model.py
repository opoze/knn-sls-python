import logging
from sklearn.neighbors import KNeighborsClassifier

class Model:
    def __init__(self):
        self.knn: KNeighborsClassifier  = None
        self.logger = logging.getLogger()

    def predict(self, vital_signs):
        try:
            return self.knn.predict([vital_signs])
        except Exception as e:
            raise e

    def set_model(self, model=None):
        self.knn = model
