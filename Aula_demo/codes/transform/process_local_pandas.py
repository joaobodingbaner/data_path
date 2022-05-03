import pandas as pd
import os 





class TransformLocal:
    def __init__(self, account_number, bucket_raw_prefix = "raw", bucket_analytics_prefix = "analytics"):
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        
    def read_json_local_file(self, filename:str) -> pd.DataFrame:
        read_json_path = f"{self.dir_path}\{filename}"
        try:
            df = pd.read_json(read_json_path, orient='records')
            print ("hello")
            return df
        except ValueError as val_error:
            print (val_error)
            return 



    def process_local(self, read_json_path):
        try:
            df_bitcoin_trades = pd.read_json(read_json_path, orient='records')
        except ValueError as val_error:
            print (val_error)

        # print(df_bitcoin_trades.head())

# process_local(json_path)