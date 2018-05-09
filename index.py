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
cnx = mysql.connector.connect(user='root', password='MySQL0000',
                              host='127.0.0.1',
                              database='github_avatars')
#conn = pymysql.connect(host='localhost', port=port_no, user='db_user', passwd='password', db='db_name')
cursor = cnx.cursor()
cnx.autocommit=True
#cnx.autocommit(True) #python3
#cursor.execute("""
#  select * from maintable
#    """)
#result = cursor.fetchall()
astart = 11
aend   = 10000+1
opener = urllib.request.FancyURLopener({})



for x in range(astart, aend):
    url = "https://avatars3.githubusercontent.com/u/"+str(x)
    #print(url)
    f = opener.open(url)
    content = f.read()
    str_content = str(content)
    #print hashlib.md5("whatever your string is").hexdigest() #python 2.7
    hash_content= hashlib.md5(str_content.encode('utf-8')).hexdigest()
    cursor.execute("""
         insert into avatars (id_user, avatarh) values ( """+str(x)+", '"+hash_content+"')")
    #result = cursor.fetchall()
    
