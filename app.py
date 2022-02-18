
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

app.config['MYSQL_USER'] = 'sql5472138'
app.config['MYSQL_PASSWORD'] = 'LFLdD4CzR4'
app.config['MYSQL_HOST'] = 'sql5.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql5472138'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app) 

@app.route('/')
def home():
    return 'Home'


@app.route('/data/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE DSAPP (PatientId INTEGER, name VARCHAR(20), age INTEGER,
    gender VARCHAR(5), birthdate VARCHAR(20), address_line1 VARCHAR(30), line2 VARCHAR(20),
    zip INTEGER, state VARCHAR(20), countr
    y VARCHAR(30))''')  
    cur.execute('''INSERT INTO DSAPP VALUES (1, 'John', 20, 'null', 'null', 'null',
    'null', 11111, 'null', 'null')''')
    cur.execute('''INSERT INTO DSAPP VALUES (2, 'Mary', 20, 'null', 'null', 'null',
    'null', 11111, 'null', 'null')''')
    cur.execute('''INSERT INTO DSAPP VALUES (3, 'Jane', 20, 'null', 'null', 'null',
    'null', 11111, 'null', 'null')''')
    mysql.connection.commit()
    cur.execute ('''SELECT * FROM DSAPP''')
    results = cur.fetchall()
    print(results)
    return jsonify(results)



