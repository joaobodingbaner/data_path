import boto3    


bucket_name_raw         = "582585946471-raw-demo-datapath-us-east-1"
bucket_name_analytics   = "582585946471-analytics-demo-datapath-us-east-1"

cf_name                 = "cf-jb"

buckets_to_destroy = [bucket_name_raw, bucket_name_analytics]

s3 = boto3.resource('s3')

def empty_all_buckets(buckets_list):
    for bucket_name in buckets_list:
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()

# empty_all_buckets(buckets_to_destroy)

cf = boto3.client('cloudformation')

def detroy_cf(cf_name):
    response = cf.delete_stack(
        StackName=cf_name
    )
    return response


response = detroy_cf(cf_name)
print(response)











