import awswrangler as wr
import boto3
import pandas as pd

bucket_name_raw         = "582585946471-raw-demo-datapath-us-east-1"
bucket_name_analytics   = "582585946471-analytics-demo-datapath-us-east-1"

s3_read_path            = f"s3://{bucket_name_raw}/data_path/trades/bitcoin/"
s3_write_path           = f"s3://{bucket_name_analytics}/data_path/trades/bitcoin"

def read_json_file(read_json_path: str) -> pd.DataFrame:
    df_bitcoin_trades = wr.s3.read_json(read_json_path)
    return df_bitcoin_trades

def filter_df(df_trade: pd.DataFrame, type_column_name: str, type_value: str) -> pd.DataFrame:
    df_trade_filtered = df_trade[df_trade[type_column_name] == type_value]
    return df_trade_filtered

def write_parquet_file(df_write: pd.DataFrame, type_value: str):
    s3_write_path_parquet = f"{s3_write_path}/type_value={type_value}/{type_value}.parquet"
    wr.s3.to_parquet(df_write, s3_write_path_parquet)

df_bitcoin_trades = read_json_file(s3_read_path)

df_buy = filter_df(df_bitcoin_trades, "type", "buy")
# print((df_buy.head()))

df_sell = filter_df(df_bitcoin_trades, "type", "sell")
# print((df_sell.head()))

print (write_parquet_file(df_buy,"buy"))
print (write_parquet_file(df_sell,"sell"))
# print (type(write_parquet_file(df_buy,"buy")))

