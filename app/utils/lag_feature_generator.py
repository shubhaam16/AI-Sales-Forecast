import pandas as pd 

class LagFeaturesGenerator:

    @staticmethod
    def generate(df : pd.DataFrame , target_column:str, lags=(1,7,30)):

        egineered_df = df.copy()

        for lag in lags:
            egineered_df [f"{target_column}_lag_{lag}"]  = (egineered_df[target_column].shift(lag))

        return egineered_df