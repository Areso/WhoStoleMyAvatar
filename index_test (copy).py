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


def getConnection():
    try:
        cnx = mysql.connector.connect(user='root', password='MySQL860000',
             host='127.0.0.1',
             database='github_avatars')
        # conn = pymysql.connect(host='localhost', port=port_no, user='db_user', passwd='password', db='db_name')
        cursor = cnx.cursor()
        cnx.autocommit=True
        return;
    except Exception:
        print("there was an error related to local database connection")
        sleep(20)
        return;


def myfunc():
    try:
    	getConnection()
        content = f.read()
        str_content = str(content)
        #print hashlib.md5("whatever your string is").hexdigest() #python 2.7
        hash_content= hashlib.md5(str_content.encode('utf-8')).hexdigest()
        cursor.execute("""
            insert into avatars (id_user, avatarh) values ( """+str(x)+", '"+hash_content+"')")
        #result = cursor.fetchall()
        return;
    except Exception:
        print("there was an error"+str(datetime.datetime.now()))
        sleep(20)
        myfunc()
        return;


# cnx.autocommit(True) #python3
# cursor.execute("""
#   select * from maintable
#     """)
# result = cursor.fetchall()
astart = 3335016
aend   = 5000000+1
opener = urllib.request.FancyURLopener({})

def url_opener(delaytime):
    try:
        delay(delaytime)
        


for x in range(astart, aend):
    url = "https://avatars3.githubusercontent.com/u/"+str(x)
    #print(url)
    ds = 1;
    try:
        f = opener.open(url)
    except Exception:
        ds = ds * 2        
        sleep(ds)
        print("there was a delay on "+str(ds)+" on UID "+str(x))
        try:
            f = opener.open(url)
        except Exception:
            ds = ds * 2
            sleep(ds)
            print("there was a delay on "+str(ds)+" on UID "+str(x))
            try:
                f = opener.open(url)
            except Exception:
                ds = ds * 2
                sleep(ds)
                print("there was a delay on "+str(ds)+" on UID "+str(x))
                try:
                    f = opener.open(url)
                except Exception:
                    ds = ds * 2
                    sleep(ds)
                    print("there was a delay on "+str(ds)+" on UID "+str(x))
                    try:
                        f = opener.open(url)
                    except Exception:
						ds = ds * 2
                        sleep(ds)
                        print("there was a delay on "+str(ds)+" on UID "+str(x))
                        try:
                            f = opener.open(url)
                        except Exception:
                            sleep(ds)
                            print("there was a delay on "+str(ds)+" on UID "+str(x))
                            try:
                                f = opener.open(url)
                            except Exception:
                                sleep(240)#4m
                                try:
                                    f = opener.open(url)
                                except Exception:
                                    sleep(480)
                                    try:
                                        f = opener.open(url)
                                    except Exception:
                                        sleep(960)#15m
                                        try:
                                            f = opener.open(url)
                                        except Exception:
                                            sleep(1920)#30m
                                            try:
                                                f = opener.open(url)
                                            except Exception:
                                                sleep(4000)#1h
                                                try:
                                                    f = opener.open(url)
                                                except Exception:
                                                    sleep(8000)#2h
                                                    try:
                                                        f = opener.open(url)
                                                    except Exception:
                                                        sleep(16000)#4h
                                                        try:
                                                            f = opener.open(url)
                                                        except Exception:
                                                            sleep(32000)#8h
                                                            try:
                                                                f = opener.open(url)
                                                            except Exception:
                                                                sleep(64000)#16h																
                                                                try:
                                                                    f = opener.open(url)
                                                                except Exception:
                                                                    print("there was an fatal error, my friend "+str(x))
    myfunc()
