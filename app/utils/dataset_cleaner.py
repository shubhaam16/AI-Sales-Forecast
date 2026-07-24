import pandas as pd

from app.utils.datatype_detector import DataTypeDetector
from app.utils.duplicate_handler import DuplicateHandler
from app.utils.missing_value_handler import MissingValueHandler


class DatasetCleaner:

    @staticmethod
    def clean(df: pd.DataFrame):

        report = {
            "original_rows": len(df),
            "original_columns": len(df.columns),
            "missing_values_before": int(df.isnull().sum().sum()),
            "duplicate_rows_before": int(df.duplicated().sum())
        }

        column_types = DataTypeDetector.detect(df)

        cleaned_df, removed_duplicates = DuplicateHandler.remove_duplicates(df)

        cleaned_df = MissingValueHandler.handle(cleaned_df,column_types)

        report["removed_duplicates"] = removed_duplicates

        report["missing_values_after"] = int(
            cleaned_df.isnull().sum().sum()
        )

        report["duplicate_rows_after"] = int(
            cleaned_df.duplicated().sum()
        )

        report["final_rows"] = len(cleaned_df)

        report["column_types"] = column_types

        return cleaned_df, report