#TODO
# Criar codigo para popular os buckets via codigo

import awswrangler as wr
import boto3
import pandas as pd

BUCKET_NAME_RAW         = "582585946471-raw-demo-datapath-us-east-1"
BUCKET_NAME_ANALYTICS   = "582585946471-analytics-demo-datapath-us-east-1"

s3_read_path            = f"s3://{BUCKET_NAME_RAW}/data_path/aula_demo/mercadobitcoin/trades/bitcoin/"
s3_write_path           = f"s3://{BUCKET_NAME_ANALYTICS}/data_path/aula_demo/mercadobitcoin/trades/bitcoin"

class TransformLocal:
    def __init__(self, account_number, bucket_raw_prefix = "raw", bucket_analytics_prefix = "analytics"):
        self.bucket_name_raw = f"{account_number}-{bucket_raw_prefix}-demo-datapath-us-east-1"
        self.bucket_name_analytics = f"{account_number}-{bucket_analytics_prefix}-demo-datapath-us-east-1"

    def read_json_file(read_json_prefix: str) -> pd.DataFrame:
        """Read a json path from s3

        Parameters
        ----------
        read_json_prefix: str
            Full prefix from s3 parh including s3://<BUCKET-NAME>/prefix/
        Returns
        -------
        A pandas dataframe based in wr.s3.read_json.

        """
        df_bitcoin_trades = wr.s3.read_json(read_json_path)
        return df_bitcoin_trades

    def filter_df(df: pd.DataFrame, type_column_name: str, type_value: str) -> pd.DataFrame:
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
        df_filtered = df[df[type_column_name] == type_value]
        return df_filtered

    def write_parquet_file(df_write: pd.DataFrame, type_value: str): #TODO 
        """ Write dataframe in the parquet format in s3.

        Parameters
        ----------
        df_write: pandas.DataFrame
            dataframe which will be written.
        type_value: str
            Column name which will be used in the partition.

        """
        s3_write_path_parquet = f"{s3_write_path}/type_value={type_value}/{type_value}.parquet"
        wr.s3.to_parquet(df_write, s3_write_path_parquet)

# df_bitcoin_trades = read_json_file(s3_read_path)
# print (df_bitcoin_trades.head())
# df_buy = filter_df(df_bitcoin_trades, "type", "buy")
# # print((df_buy.head()))

# df_sell = filter_df(df_bitcoin_trades, "type", "sell")
# # print((df_sell.head()))

# print (write_parquet_file(df_buy,"buy"))
# print (write_parquet_file(df_sell,"sell"))
# print (type(write_parquet_file(df_buy,"buy")))
