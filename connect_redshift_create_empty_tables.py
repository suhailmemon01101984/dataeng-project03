#to make this code work i had to login to aws console and do 2 things.
#1. go into security groups and add an inbound rule that allows all tcp, any ipv4 traffic
#2. go into redshift serverless and turn publicly accessible to ON


import redshift_connector
conn = redshift_connector.connect(
     host='default-workgroup.236765750193.us-east-1.redshift-serverless.amazonaws.com',
     database='dev',
     port=5439,
     user='suhailmemon84-admin',
     password='May200726'
  )

cursor = conn.cursor()

cursor.execute("select * from dev.public.shoes")
result: tuple = cursor.fetchall()
print(result)

####create empty tables
