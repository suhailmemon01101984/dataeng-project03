###pre requisite: login to aws console and go under roles and created the custom role: suhailmemon84-reshift-s3-readonly-access
#### then go under redshift click your name space --> security & encryption --> associate iam role --> associate the role you created above with redshift and save
###this role allows redshift read access to s3 via the attached policy: AmazonS3ReadOnlyAccess
###explanation as to why a role is needed here: https://medium.com/@lucadefra92/stage-data-from-s3-to-redshift-a6c8f80e3b7
### once you have the role get the role arn. in my case it was-> arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access

import redshift_connector
conn = redshift_connector.connect(
     host='default-workgroup.236765750193.us-east-1.redshift-serverless.amazonaws.com',
     database='dev',
     port=5439,
     user='suhailmemon84-admin',
     password='mypwd'
  )
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("truncate table dev.public.event")
cursor.execute("copy dev.public.event from 's3://tickit-data-bucket/allevents_pipe.txt' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' delimiter '|';")


cursor.execute("truncate table dev.public.users")
cursor.execute("copy dev.public.users from 's3://tickit-data-bucket/allusers_pipe.txt' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' delimiter '|';")


cursor.execute("truncate table dev.public.category")
cursor.execute("copy dev.public.category from 's3://tickit-data-bucket/category_pipe.txt' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' delimiter '|';")


cursor.execute("truncate table dev.public.date")
cursor.execute("copy dev.public.date from 's3://tickit-data-bucket/date2008_pipe.txt' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' delimiter '|';")

cursor.execute("truncate table dev.public.listing")
cursor.execute("copy dev.public.listing from 's3://tickit-data-bucket/listings_pipe.txt' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' delimiter '|';")

cursor.execute("truncate table dev.public.sales")
cursor.execute("copy dev.public.sales from 's3://tickit-data-bucket/sales_tab.txt' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' timeformat 'MM/DD/YYYY HH:MI:SS' delimiter '\t';")

cursor.execute("truncate table dev.public.venue")
cursor.execute("copy dev.public.venue from 's3://tickit-data-bucket/venue_pipe.txt' iam_role 'arn:aws:iam::236765750193:role/suhailmemon84-reshift-s3-readonly-access' delimiter '|';")


cursor.close()
conn.close()