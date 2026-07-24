import pandas as pd


class DataTypeDetector:

    @staticmethod
    def detect(df: pd.DataFrame):

        detected_types = {}

        for column in df.columns:

            if pd.api.types.is_numeric_dtype(df[column]):
                detected_types[column] = "numeric"

            elif pd.api.types.is_datetime64_any_dtype(df[column]):
                detected_types[column] = "datetime"

            else:

                try:
                    pd.to_datetime(df[column])

                    detected_types[column] = "datetime"

                except Exception:

                    detected_types[column] = "categorical"

        return detected_types