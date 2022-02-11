

from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'sql5472138'
app.config['MYSQL_PASSWORD'] = 'LFLdD4CzR4'
app.config['MYSQL_HOST'] = 'sql5.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql5472138'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app) 

@app.route('/data/')
def index():
    cur = mysql.connection.cursor()
    #cur.execute('''CREATE TABLE datascrubberapp (id INTEGER, name VARCHAR(20))''')
    #cur.execute('''INSERT INTO datascrubberapp VALUES (1, 'John')''')
    #mysql.connection.commit()
    cur.execute ('''SELECT * FROM datascrubberapp''')
    results = cur.fetchall()
    print(results)
    return results[0]['name']


