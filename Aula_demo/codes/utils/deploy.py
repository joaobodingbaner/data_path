import boto3
from datetime import datetime

now = datetime.now()
bucket_name_raw = "582585946471-raw-demo-datapath-us-east-1"
json_path = "C:\\Users\\joaov\\Desktop\\coding\\git_repos\\data_path\\Aula_demo\\codes\\transform\\example_bitcoin.json"
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

def upload_json_file():
    s3 = boto3.resource('s3')
    prefix_path = (f"data_path/aula_demo/mercadobitcoin/trades/bitcoin/year={year}/month={month}/day={day}/bitcoin.json")
    print ("hello")
    response = s3.meta.client.upload_file(json_path, bucket_name_raw, prefix_path)
    print(response)

upload_json_file()

