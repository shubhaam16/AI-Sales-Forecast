from app.utils.date_feature_extractor import DateFeatureExtractor
from app.utils.lag_feature_generator import LagFeaturesGenerator
from app.utils.rolling_feature_generator import RollingfeaturesGenerator

class FeatureEngineering:
    @staticmethod
    def transform(df , target_column = "Sales"):
        engineered_df = DateFeatureExtractor.extract(df)
        engineered_df = LagFeaturesGenerator.generate(engineered_df,target_column)
        engineered_df = RollingfeaturesGenerator.generate(engineered_df,target_column)

        return engineered_df