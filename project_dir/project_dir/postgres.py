import psycopg

data_connection = "dbname=my_db user=postgres password=superpassword host='django_sql' port=5432"

# docker-compose  и докер хочет хост по имени сервиса ПОРА ЗАПОМНИТЬ!!!

create_table_query = """CREATE TABLE items_table
(
    id   serial NOT NULL PRIMARY KEY, 
    data jsonb  NOT NULL
);"""


insert_query_sql = '''
            INSERT INTO items_table(data) 
            VALUES (%s)
            RETURNING data
            '''
#---class connector

class DB(object):
    def __init__(self):
        self._conn = psycopg.connect(data_connection)
    def cursor_executor(self,sql_command,*args):
        with self._conn.cursor() as cur:
            cur.execute(sql_command,*args)
            print(args)
            return args
    def fetch__one(self):
        with self._conn.cursor() as cur:
            result = cur.fetchone()
            print(result)
            return result
    def fetch__many(self,result):
        with self._conn.cursor() as cur:
            result = cur.fetchmany()
            print(result)
            return result
    def commiting(self):
        self._conn.commit()
        print("DB Committed !")



init_db = DB()
