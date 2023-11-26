import boto3
def s3_upload_file(file,bucket):
    filename=f'./datafiles/{file}'
    s3 = boto3.client('s3')
    s3.upload_file(filename,bucket,file)


s3_upload_file('allevents_pipe.txt','tickit-data-bucket')
s3_upload_file('allusers_pipe.txt','tickit-data-bucket')
s3_upload_file('category_pipe.txt','tickit-data-bucket')
s3_upload_file('date2008_pipe.txt','tickit-data-bucket')
s3_upload_file('listings_pipe.txt','tickit-data-bucket')
s3_upload_file('sales_tab.txt','tickit-data-bucket')
s3_upload_file('venue_pipe.txt','tickit-data-bucket')


