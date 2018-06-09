#!/usr/bin/env python3
# #!/usr/bin/python3
import mysql.connector
import hashlib
from time import sleep
from time import ctime
import datetime
import os
import subprocess

# import pymysql #for python3
# sudo apt-get install python-pip
# sudo apt-get install python3-pip
# sudo pip install mysql-connector #python 2.7
# sudo pip install mysql-connector-python
# sudo pip3 install mysql-connector-python #python3.3
LocalTime = str(datetime.datetime.now().time())

cnx = mysql.connector.connect(user='root', password='MySQL0000',
             host='127.0.0.1',
             database='github_avatars')
#conn = pymysql.connect(host='localhost', port=port_no, user='db_user', passwd='password', db='db_name')
mycursor = cnx.cursor()
cnx.autocommit=True
restart  = False;
mycurrid = 0;

def myread_watchdog(mycursor):
    global restart
    try:
        mycursor.execute("SELECT * FROM `watchdog` ORDER BY id_record DESC LIMIT 0 , 2")
        result = mycursor.fetchall()
        #countr = 0
        myresl = []
        for row in result:
            myresl.append(row[1])
        if (len(myresl)==2):
            if (myresl[0]==myresl[1]):
                restart = True;
		mycursor.execute("insert into reboots (id_record, datetime) values (null, null)")   
                #args = ["sudo restart -now"]
                #process = subprocess.Popen("sudo restart", stdout=subprocess.PIPE)
                #process = subprocess.call("sudo reboot", shell=True)
                print("reboot")
        return restart;
    except Exception as e:
        print("there was an error "+str(datetime.datetime.now())+" "+str(e))
        return;

def mywrite_watchdog(mycursor):
    try:
        mycursor.execute("insert into watchdog (id_record, pos, datetime) values (null, "+str(mycurrid)+", null)")
        return;
    except Exception as e:
        print("there was an error "+str(datetime.datetime.now())+" "+str(e))
        return;


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
mywrite_watchdog(mycursor)
myread_watchdog(mycursor)
