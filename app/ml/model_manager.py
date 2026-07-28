import joblib
from pathlib import Path


class ModelManager:

    MODEL_DIR = Path("saved_models")
    MODEL_DIR.mkdir(exist_ok=True)

    @staticmethod
    def save(model,filename):
        path = ModelManager.MODEL_DIR / filename

        joblib.dump(model,path)

        return path

    @staticmethod
    def load(filename):

        path = ModelManager.MODEL_DIR / filename

        return joblib.load(path)