from core import *
import psycopg2.extras

conn = None
cur = None

try:
    with psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        port=DB_PORT,
        password=DB_PASS
    ) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute("DROP TABLE IF EXISTS employee")

            create_script = """
                CREATE TABLE IF NOT EXISTS employee(
                id int PRIMARY KEY,
                name varchar(40) NOT NULL,
                salary int,
                dept_id varchar(30)
                )"""

            cur.execute(create_script)

            insert_script = "INSERT INTO employee (id, name, salary, dept_id) VALUES ( %s, %s, %s, %s )"
            insert_value = [(1, "James", 12000, 'D1'), (2, "Robin", 10000, 'D1'), (3, "James", 12000, 'D1'),
                            (4, "Robin", 10000, 'D1')]

            for x in insert_value:
                cur.execute(insert_script, x)

            update_script = "UPDATE employee SET salary = salary + (salary * 0.5)"
            cur.execute(update_script)

            delete_script = "DELETE FROM employee WHERE name = %s"
            delete_value = ("James",)
            cur.execute(delete_script, delete_value)

            cur.execute('SELECT * FROM EMPLOYEE')
            for x in cur.fetchall():
                print(x['name'], x['salary'])

            # conn.commit()

except Exception as err:
    print(err)
finally:
    # if cur is not None:
    #     cur.close()

    if conn is not None:
        conn.close()
