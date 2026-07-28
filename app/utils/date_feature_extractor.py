import pandas as pd


class DateFeatureExtractor:

    @staticmethod
    def extract(df: pd.DataFrame):

        cleaned_df = df.copy()

        datetime_columns = cleaned_df.select_dtypes(include=["datetime64[ns]"]).columns

        for column in datetime_columns:

            cleaned_df[f"{column}_year"] = cleaned_df[column].dt.year

            cleaned_df[f"{column}_month"] = cleaned_df[column].dt.month

            cleaned_df[f"{column}_day"] = cleaned_df[column].dt.day

            cleaned_df[f"{column}_day_of_week"] = (cleaned_df[column].dt.dayofweek)

            cleaned_df[f"{column}_quarter"] = (cleaned_df[column].dt.quarter)

            cleaned_df[f"{column}_week"] = (cleaned_df[column].dt.isocalendar().week.astype(int))

        return cleaned_df