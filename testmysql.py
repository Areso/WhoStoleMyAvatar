import mysql.connector
import hashlib
#import pymysql #for python3
#sudo apt-get install python-pip
#sudo apt-get install python3-pip
#sudo pip install mysql-connector #python 2.7
#sudo pip install mysql-connector-python
#sudo pip3 install mysql-connector-python #python3.3
#import urllib
import urllib.request
cnx = mysql.connector.connect(user='root', password='MySQLInternet0000',
                              host='127.0.0.1',
                              database='mysql')
#conn = pymysql.connect(host='localhost', port=port_no, user='db_user', passwd='password', db='db_name')
print(type(cnx))
