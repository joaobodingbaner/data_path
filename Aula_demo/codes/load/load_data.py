#TODO ajustar script

import awswrangler as wr
import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine

bucket_name_analytics   = "582585946471-analytics-demo-datapath-us-east-1"

s3_read_path            = f"s3://{bucket_name_analytics}/data_path/aula_demo/mercadobitcoin/trades/bitcoin/"

def read_parquet_file(read_parquet_path: str) -> pd.DataFrame:
    df_bitcoin_trades = wr.s3.read_parquet(read_parquet_path)
    return df_bitcoin_trades

def rename_adapt_schema_table(df):
    df.rename(columns = {'type':'type_trade', 'date':'date_trade'}, inplace = True)
    return df
df = read_parquet_file(s3_read_path)


def load_data_to_postgres (df_write, table_name):
    engine = create_engine('postgresql://<user>:<pwd>@<host>:5432/<db_name>')
    meta = sqlalchemy.MetaData(engine, schema='aulademo')
    meta.reflect()
    pdsql = pd.io.sql.SQLDatabase(engine, meta=meta)
    pdsql.to_sql(df, table_name, if_exists='append', index=False)

df_parquet = read_parquet_file(s3_read_path)
df_renamed = rename_adapt_schema_table(df_parquet)
load_data_to_postgres(df_renamed, "tb_bitcoin_trades_buy")