from grab import Grab
import mysql.connector

g = Grab(log_file='out.html')
g.setup(proxy='localhost:6588', proxy_type='http')

g.go('http://localhost/blog/')

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'myspider_web',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

test_q = ("INSERT INTO TEST"
          "(id) "
          "VALUES (2)")

cursor.execute(test_q)



cnx.commit()
cursor.close()
cnx.close()
