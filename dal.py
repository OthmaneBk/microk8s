from psycopg2 import connect
from psycopg2.extensions import connection

def create_connection()->connection|Exception:
    try :
        cnx:connection=connect(
            host='db',
            user='admin',
            password=1234,
            database='db_ms'
        )
        return cnx
    except Exception as e:
        return e
