import pandas as pd


class MissingValueHandler:

    @staticmethod
    def handle(df: pd.DataFrame, column_types: dict):

        cleaned_df = df.copy()

        for column in cleaned_df.columns:

            if column_types[column] == "numeric":
                cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].median())

            elif column_types[column] == "datetime":
                cleaned_df[column] = pd.to_datetime(cleaned_df[column],errors="coerce")
                cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].mode()[0])

            else:
                cleaned_df[column] = cleaned_df[column].fillna("Unknown")

        return cleaned_df