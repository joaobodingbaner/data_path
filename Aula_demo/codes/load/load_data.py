import awswrangler as wr
import boto3
import pandas as pd

bucket_name_analytics   = "582585946471-analytics-demo-datapath-us-east-1"

s3_read_path            = f"s3://{bucket_name_analytics}/data_path/trades/bitcoin/"

def read_parquet_file(read_parquet_path: str) -> pd.DataFrame:
    df_bitcoin_trades = wr.s3.read_parquet_path(read_parquet_path)
    return df_bitcoin_trades

df = read_parquet_file(s3_read_path)