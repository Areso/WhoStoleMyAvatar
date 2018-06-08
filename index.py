#!/usr/bin/env python3
# #!/usr/bin/python3
import mysql.connector
import hashlib
from time import sleep
from time import ctime
import datetime
import os
# import pymysql #for python3
# sudo apt-get install python-pip
# sudo apt-get install python3-pip
# sudo pip install mysql-connector #python 2.7
# sudo pip install mysql-connector-python
# sudo pip3 install mysql-connector-python #python3.3
# import urllib
import urllib.request
LocalTime = str(datetime.datetime.now().time())

cnx = mysql.connector.connect(user='root', password='MySQL0000',
             host='127.0.0.1',
             database='github_avatars')
#conn = pymysql.connect(host='localhost', port=port_no, user='db_user', passwd='password', db='db_name')
mycursor = cnx.cursor()
cnx.autocommit=True
# result = cursor.fetchall()

def myread_avatars(mycursor):
    global mycurrid
    try:
        mycursor.execute("SELECT id_user FROM `avatars` ORDER BY id_user DESC LIMIT 0 , 1")
        resulta = mycursor.fetchall()
        for row in resulta:
            mycurrid = row[0]
        return mycurrid;
    except Exception as e:
        print("there was an error "+str(datetime.datetime.now())+" "+str(e))
        return;

myread_avatars(mycursor)
astart = mycurrid+1
aend   = 50000000+1
opener = urllib.request.FancyURLopener({})

def url_opener(delaytime, url, x, mystarted):
    if (x%10000==0 or mystarted==True):
        mystarted  = False
        #mycursor = getConnection()
    try:
        f = opener.open(url)
        myfunc(f, mycursor)
        delaytime = 0
    except Exception as e:
        delaytime = delaytime+1
        delaytime = delaytime*2
        print("there was a delay on "+str(delaytime)+" on UID "+str(x)+" "+str(datetime.datetime.now())+" "+str(e))
        sleep(delaytime)
        url_opener(delaytime, url, x, mystarted)


def myfunc(f, mycursor):
    try:
        content      = f.read()
        str_content  = str(content)
        #print hashlib.md5("whatever your string is").hexdigest() #python 2.7
        hash_content = hashlib.md5(str_content.encode('utf-8')).hexdigest()
        mycursor.execute("""
            insert into avatars (id_user, avatarh) values ( """+str(x)+", '"+hash_content+"')")
        #mycursor.execute("""insert into avatars (id_user, avatarh) values (5000000, 'asd')""")
        #result = cursor.fetchall()
        return;
    except Exception as e:
        print("there was an error "+str(datetime.datetime.now())+" "+str(e))
        sleep(20)
        myfunc(f, mycursor)
        return;

cursor    = 0;
mystarted = True
for x in range(astart, aend):
    url = "https://avatars3.githubusercontent.com/u/"+str(x)
    #print(url)
    url_opener(0, url, x, mystarted)

