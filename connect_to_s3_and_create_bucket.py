import boto3

# pre req: create a user, grant that user s3 rw access in aws console and download the creds of the user to get your access key id and the secret key

# you can either connect to aws from command line as shown below.
# s3=boto3.resource(service_name='s3',region_name='us-east-1',aws_access_key_id='<your access key id>',aws_secret_access_key='<your aws secret access key>')
# for bucket in s3.buckets.all():
#     print(bucket.name)


# or you can connect to aws as shown below by using a config file. for this to work you need to ensure that you have setup aws on your laptop with these dirs:
# M-C02X39EQJG5J:.aws suhailmemon$ pwd
# /Users/suhailmemon/.aws
# M-C02X39EQJG5J:.aws suhailmemon$ ls -ltr
# total 16
# -rw-r--r--  1 suhailmemon  staff  116 Nov 26 14:51 credentials
# -rw-r--r--  1 suhailmemon  staff   27 Nov 26 14:52 config
# M-C02X39EQJG5J:.aws suhailmemon$ cat credentials
# [default]
# aws_access_key_id = <your access key id>
# aws_secret_access_key = <your aws secret access key>
# M-C02X39EQJG5J:.aws suhailmemon$ cat config
# [default]
# region=us-east-1
# M-C02X39EQJG5J:.aws suhailmemon$

def bucket_exists(bucket):
  s3 = boto3.resource('s3')
  return s3.Bucket(bucket) in s3.buckets.all()


s3 = boto3.client('s3')

if bucket_exists('tickit-data-bucket')==True:
    print('bucket exists')
else:
    s3.create_bucket(Bucket='tickit-data-bucket')

response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print(buckets)

