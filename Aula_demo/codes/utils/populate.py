from transform.process_local_datawrangler import TransformLocal

transf = TransformLocal()

class PopulateParquet():
    def create_parquet_file(self, type_value : str):
        if type_value == "buy" or type_value == "sell":
            df_trades = transf.read_json_file(read_json_prefix="data_path/aula_demo/mercadobitcoin/trades/bitcoin/")
            df_trades_filtered_buy = transf.filter_df(df_trades,"type",type_value)
            transf.write_parquet_file(df_trades_filtered_buy,type_value)
        else:
            raise ValueError("Must be buy or sell")
    # print (df_trades_filtered_buy)