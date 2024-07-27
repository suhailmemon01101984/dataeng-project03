#to make this code work i had to login to aws console and do 2 things.
#1. go into security groups and add an inbound rule that allows all tcp, any ipv4 traffic
#2. go into redshift serverless and turn publicly accessible to ON


import redshift_connector
conn = redshift_connector.connect(
     host='default-workgroup.236765750193.us-west-2.redshift-serverless.amazonaws.com',
     database='dev',
     port=5439,
     user='suhailmemon84-admin',
     password='mypwd'
  )
conn.autocommit = True
cursor = conn.cursor()

####create empty tables

cursor.execute("""\
create table if not exists dev.public.category(
catid integer not null,
catgroup varchar(10),
catname varchar(10),
catdesc varchar(50),
primary key(catid)
)
distkey(catid)""")

cursor.execute("""\
create table if not exists dev.public.venue(
venueid integer not null,
venuename varchar(100),
venuecity varchar(30),
venuestate char(2),
venueseats integer,
primary key(venueid)
)
distkey(venueid)""")

cursor.execute("""\
create table if not exists dev.public.date(
dateid integer not null,
caldate date not null,
day varchar(3) not null,
week integer not null,
month varchar(5) not null ,
qtr varchar(5) not null,
year integer not null encode mostly8,
holiday boolean,
primary key(dateid)
)
distkey(dateid)""")

cursor.execute("""\
create table if not exists dev.public.users(
userid integer not null,
username varchar(8),
firstname varchar(30),
lastname varchar(30),
city varchar(30),
state char(2),
email varchar(100),
phone varchar(14),
likesports boolean,
liketheatre boolean,
likeconcerts boolean,
likejazz boolean,
likeclassical boolean,
likeopera boolean,
likerock boolean,
likevegas boolean,
likebroadway boolean,
likemusicals boolean,
primary key(userid)
)
distkey(userid)""")

cursor.execute("""\
create table if not exists dev.public.event(
eventid integer not null,
venueid integer not null,
catid integer not null,
dateid integer not null,
eventname varchar(200),
starttime timestamp,
primary key(eventid),
foreign key(venueid) references dev.public.venue(venueid),
foreign key(catid) references dev.public.category(catid),
foreign key(dateid) references dev.public.date(dateid)
)
distkey(eventid)""")

cursor.execute("""\
create table if not exists dev.public.listing(
listid integer not null,
sellerid integer not null,
eventid integer not null,
dateid integer not null,
numtickets integer not null,
priceperticket decimal(8,2) ,
totalprice decimal(8,2) ,
listtime timestamp,

primary key(listid),
foreign key(sellerid) references dev.public.users(userid),
foreign key(eventid) references dev.public.event(eventid),
foreign key(dateid) references dev.public.date(dateid)
)
distkey(listid)""")

cursor.execute("""\
create table if not exists dev.public.sales(
salesid integer not null,
listid integer not null,
sellerid integer not null,
buyerid integer not null,
eventid integer not null ,
dateid smallint not null,
qtysold smallint not null ,
pricepaid decimal(8,2) ,
commission decimal(8,2) ,
saletime timestamp,
primary key(salesid),
foreign key(listid) references dev.public.listing(listid),
foreign key(sellerid) references dev.public.users(userid),
foreign key(buyerid) references dev.public.users(userid),
foreign key(dateid) references dev.public.date(dateid)
)
distkey(salesid)""")

cursor.close()
conn.close()

