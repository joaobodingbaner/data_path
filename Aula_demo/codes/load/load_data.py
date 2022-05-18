#TODO ajustar script

import awswrangler as wr
import pandas as pd
import sqlalchemy

bucket_name_analytics = "582585946471-analytics-demo-datapath-us-east-1"
s3_read_path = f"s3://{bucket_name_analytics}/data_path/aula_demo/mercadobitcoin/trades/bitcoin/"

class LoadDataPostgresRDS:


    def read_parquet_file(self, read_parquet_path: str) -> pd.DataFrame:
        df_bitcoin_trades = wr.s3.read_parquet(read_parquet_path)
        return df_bitcoin_trades

    def rename_adapt_schema_table(self, df: pd.DataFrame) -> pd.DataFrame:
        df.rename(columns = {'type':'type_trade', 'date':'date_trade'}, inplace = True)
        return df
    df = read_parquet_file(s3_read_path)

    def load_data_to_postgres(self, df_write: pd.DataFrame, table_name: str, username: str, pwd: str, host: str, db_name:str):
        engine = sqlalchemy.create_engine(
            f'postgresql://{username}:{pwd}@{host}:5432/{db_name}')
        meta = sqlalchemy.MetaData(engine, schema='aulademo')
        meta.reflect()
        pdsql = pd.io.sql.SQLDatabase(engine, meta=meta)
        pdsql.to_sql(df_write, table_name, if_exists='append', index=False)


df_parquet = LoadDataPostgresRDS().read_parquet_file(s3_read_path)
df_renamed = LoadDataPostgresRDS().rename_adapt_schema_table(df_parquet)
LoadDataPostgresRDS().load_data_to_postgres(df_renamed, "tb_bitcoin_trades_buy")