import pandas as pd


class DatasetAnalyzer:

    @staticmethod
    def analyze(df: pd.DataFrame):
        missing_vaules= df.isnull().sum()
        return {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),

            "missing_values": int(missing_vaules.sum()),

            "duplicate_rows": int(df.duplicated().sum()),

            "data_types": {
                column: str(dtype)
                for column, dtype in df.dtypes.items()
            }
        }