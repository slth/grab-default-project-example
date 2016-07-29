# coding=UTF8
import csv

rid = 1
category = 90
user_id = 0
rtype = 'p'
rautor = "spider.alekseysavin.com"
title = "test"
email = "i@alekseysavin.com"
city = "Moscow"
city_id = 40
url = "http://spider.alekseysavin.com"
click = 0
contacts = "me@alekseysavin.com"
text = "test"
price = 0
video = ""
hits = 0
old = "old"
mess = 0
rcheked = 0
checkbox_top = 0
top_time = 0
send_notice_vip_sms = 0
checkbox_select = 0
select_time = 0
send_notice_select_sms = 0
tags = 0
send_notice_day = 0
time_delete = 0
date_add = 0
x1 = 0
x2 = 0
x3 = "0000-00-00"
x4 = "00:00:00"
x5 = 0
x6 = "test"
x7 = 0
x8 = 30
x9 = "2016-07-26"
x10 = "19:47:07"

with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_ALL)
    spamwriter.writerow([rid,
                        category,
                        user_id,
                        rtype,
                        rautor,
                        title,
                        email,
                        city,
                        city_id,
                        url,
                        click,
                        contacts,
                        text,
                        price,
                        video,
                        hits,
                        old,
                        mess,
                        rcheked,
                        checkbox_top,
                        top_time,
                        send_notice_vip_sms,
                        checkbox_select,
                        select_time,
                        send_notice_select_sms,
                        tags,
                        send_notice_day,
                        time_delete,
                        date_add,
                        x1,
                        x2,
                        x3,
                        x4,
                        x5,
                        x6,
                        x7,
                        x8,
                        x9,
                        x10
                         ])

print "Формирование xml закончено"