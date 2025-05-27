from abc import ABC, abstractmethod

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

class ModelTrain(ABC):
    @abstractmethod
    def train(self, X_train, y_train):
        pass


class RegressionModelTraining(ModelTrain):
    def train(self, X_train, y_train):
        pass
    
class ModelTraining():
    def __init__(self, model_type):
        self.model_type = model_type

    def set_model_type(self, type):
        self.model_type = type

    def execute_model_training(self, X_train, y_train):
        return self.model_type.train(X_train, y_train)


if __name__ == "__main__":
    pass