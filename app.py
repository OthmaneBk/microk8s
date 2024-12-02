from flask import Flask,jsonify
from redis import Redis
from dal import create_connection
from psycopg2.extensions import connection
app=Flask(__name__)
cache=Redis('cache')
@app.route('/')
def index():
    cache.incr('counter')
    return '<html><center><h1 style="color:blue">Hello from Docker :'+cache.get("counter").decode()+'</h1></center></html>'

@app.route('/users')
def users():
    cnx:connection|Exception=create_connection()
    if isinstance(cnx,connection) :
        cursor=cnx.cursor()
        cursor.execute('SELECT * FROM T_USER;')
        return f'<html><center><h1 style="color:blue">{jsonify(cursor.fetchall())}</h1></center></html>'
    return f'<html><center><h1 style="color:blue">Connection Error</h1></center></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)