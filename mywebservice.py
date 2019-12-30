import sqlite3

from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store;")
    rows = cur.fetchall()
    for row in rows:
        print (row)
    return jsonify(rows)

if __name__=='__main__':
    app.run(debug=True)
