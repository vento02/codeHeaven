import pandas as pd
import pymysql

config = {
    'host' : 'localhost',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'db',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    cursor.execute("show tables")
    tables = cursor.fetchall()

    sw=False
    if tables:
        for table in tables:

            if table[0] =='score_tab':
                sw=True

    if sw:
        sql="select * from score_tab"
        cursor.execute(sql)
        records = cursor.fetchall()

        for record in records:
            print(record)
        #수학점수 50에서 90점 검색
        sql="select * from score_tab where math >= 50 and math <= 90"
        cursor.execute(sql)
        records = cursor.fetchall()
        print("수학점수 50에서 90점인 행")
        for record in records:
            print(record)
        dept = int(input("출력하고싶은 반: "))
        sql=f"select * from score_tab where dept = '{dept}'"
        cursor.execute(sql)
        depts = cursor.fetchall()

        for de in depts:
            print(de)


except Exception as e:
    print("db error: ",e)

finally:
    cursor.close()
    conn.close()