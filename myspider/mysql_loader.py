# coding=UTF8
import csv
import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'doska',
  'raise_on_warnings': True,
}

csv_data = csv.reader(file('jb_board.csv'))

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

b_message = ('INSERT INTO jb_board'
             '(id, id_category, user_id, type, autor, title, email, city, city_id, url, click, contacts, text, price, video, hits, old_mess, checked, checkbox_top, top_time, send_notice_vip_sms, checkbox_select, select_time, send_notice_select_sms, tags, send_notice_day, time_delete, date_add ) '
             'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ')

b_data = csv_data

for row in csv_data:
    cursor.execute(b_message, row)

cnx.commit()
cursor.close()
cnx.close()
