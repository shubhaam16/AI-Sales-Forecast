from pydantic import BaseModel


class CleaningReportResponse(BaseModel):

    original_rows: int
    original_columns: int

    missing_values_before: int
    missing_values_after: int

    duplicate_rows_before: int
    duplicate_rows_after: int

    removed_duplicates: int

    final_rows: int

    column_types: dict[str, str]