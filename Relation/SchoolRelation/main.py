# -*- coding: utf-8 -*-

import pymysql.cursors
from school_sieve import school_sieve


config = {
    'host': '111.205.121.93',
    'user': 'root',
    'password': 'root@buaa',
    'db': 'EDMS',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

connection = pymysql.connect(**config)

p = 1000

def sele_resume(st, ed):
    try:
        with connection.cursor() as cursor:

            cur = st
            while cur < ed:
                sql = 'SELECT id, resume FROM basic_info LIMIT %s, %s'
                cursor.execute(sql, (cur, p))
                result = cursor.fetchall()
                cnt = 1
                for res in result:
                    if (res['resume'] != None and len(res['resume']) > 3):
                        abstract_shcool(res['id'], res['resume'], cursor)
                    cnt += 1
                    print(cur + cnt)
                cur += p + 1
        connection.commit()
    finally:
        connection.close();


def abstract_shcool(id, resume, cursor):
    sc_list = school_sieve(resume)
    sql = "INSERT INTO schoolmate_relation(id, school_list, profile) VALUES(%s, %s, %s) ON DUPLICATE KEY UPDATE id = %s"
    if (len(sc_list) > 0):
        # print(sc_list)
        cursor.execute(sql, (id, str(sc_list), resume, id))


if __name__ == "__main__":
    st = 576280
    ed = 1093249
    sele_resume(st, ed)