import pandas as pd
import os 

class TransformLocal:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        
    def read_json_local_file(self, filename:str) -> pd.DataFrame:
        read_json_path = f"{self.dir_path}\{filename}"
        try:
            df = pd.read_json(read_json_path, orient='records')
            return df
        except ValueError as val_error:
            print (val_error)
            return 

    def filter_df(self, df: pd.DataFrame, type_column_name: str, type_value: str) -> pd.DataFrame:
        """ Filter a dataframe based on a column.

        Parameters
        ----------
        df: pandas.DataFrame
            dataframe to be filtered.
        type_column_name: str
            Column name which will be used in the filter.
        type_value: str
            Value to be filtered in the column values
        Returns
        -------
        A pandas dataframe.

        """
        df_filtered = df[df[type_column_name] == type_value].reset_index(drop=True)
        return df_filtered


    def process_local(self, read_json_path):
        try:
            df_bitcoin_trades = pd.read_json(read_json_path, orient='records')
        except ValueError as val_error:
            print (val_error)

        # print(df_bitcoin_trades.head())

# process_local(json_path)