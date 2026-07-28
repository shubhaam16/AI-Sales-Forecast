import pandas as pd 

class RollingfeaturesGenerator:

    @staticmethod
    def generate (df :  pd.DataFrame , target_column:str , windows= (7,30)):

        engineered_df = df.copy()

        for window in windows:
            engineered_df[f"{target_column}_rolling_mean _ {window}"]= engineered_df[target_column].rolling(window).mean()

        return engineered_df