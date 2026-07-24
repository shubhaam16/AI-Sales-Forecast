import pandas as pd

class DuplicateHandler:

    @staticmethod
    def remove_duplicate(df:pd.DataFrame):
        before = len(df)

        cleaned_df= df.drop_duplicates()

        after = len(cleaned_df)

        return cleaned_df,before - after 