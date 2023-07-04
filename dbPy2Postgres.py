DB_HOST = "localhost"
DB_NAME = "northwind"
DB_USER = "postgres"
DB_PASS = "ebube"

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


    #cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    #cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, NAME VARCHAR);") # already created, commented to avoid errors

    # cur.execute("INSERT INTO student (name) VALUES(%s)", ("John",))
    # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Bobby",))
    # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Daniel",))
    # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Christina",))

    # cur.execute("SELECT * FROM student;")
    # print(cur.fetchall())

with conn:

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        # cur.execute("SELECT * FROM student WHERE id = %s;", (3,))
        # print(cur.fetchone()['name'])
        # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Janet",))

        cur.execute("SELECT * FROM student;")
        print(cur.fetchall())

        print("New-Features branch!!")

#conn.commit()

# cur.close()

conn.close()