import awswrangler as wr
import boto3
import pandas as pd

json_path = "C:\\Users\\joaov\\Desktop\\coding\\git_repos\\data_path\\Aula_demo\\codes\\transform\\example_bitcoin.json"

def process_local(read_json_path):
    df_bitcoin_trades = pd.read_json(read_json_path, orient='records')
    print(df_bitcoin_trades.head())

process_local(json_path)