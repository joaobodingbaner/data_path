import awswrangler as wr
import boto3
import pandas as pd

json_path = "C:\\Users\\joaov\\Desktop\\coding\\git_repos\\data_path\\Aula_demo\\codes\\transform\\example_bitcoin.json"

s3_path = ""
def process_local(read_json_path):
    df_bitcoin_trades = pd.read_json(read_json_path, orient='records')
    print(df_bitcoin_trades.head())

process_local(json_path)

# import json

# with open('C:\\Users\\joaov\\Desktop\\coding\\git_repos\\data_path\\Aula_demo\\codes\\transform\\example_bitcoin.json') as f:
#     print(f)
# df = wr.s3.read_json([path1, path2])

# # Storing data on Data Lake
# wr.s3.to_parquet(
#     df=df,
#     path="s3://bucket/dataset/",
#     dataset=True,
#     database="my_db",
#     table="my_table"
# )

# # Retrieving the data directly from Amazon S3
# df = wr.s3.read_parquet("s3://bucket/dataset/", dataset=True)

# # Retrieving the data from Amazon Athena
# df = wr.athena.read_sql_query("SELECT * FROM my_table", database="my_db")

# # Get a Redshift connection from Glue Catalog and retrieving data from Redshift Spectrum
# con = wr.redshift.connect("my-glue-connection")
# df = wr.redshift.read_sql_query("SELECT * FROM external_schema.my_table", con=con)
# con.close()

# # Amazon Timestream Write
# df = pd.DataFrame({
#     "time": [datetime.now(), datetime.now()],   
#     "my_dimension": ["foo", "boo"],
#     "measure": [1.0, 1.1],
# })
# rejected_records = wr.timestream.write(df,
#     database="sampleDB",
#     table="sampleTable",
#     time_col="time",
#     measure_col="measure",
#     dimensions_cols=["my_dimension"],
# )

# # Amazon Timestream Query
# wr.timestream.query("""
# SELECT time, measure_value::double, my_dimension
# FROM "sampleDB"."sampleTable" ORDER BY time DESC LIMIT 3
# """)