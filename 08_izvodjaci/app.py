import os
import sqlite3

from flask import Flask, render_template, request,g

app = Flask(__name__)

conn = sqlite3.connect(os.path.join(app.root_path, 'music.db'))

#@app.route("/", methods=["GET", "POST"])


def get_db():
    if not "_db_conn" in g:
        g._db_conn = sqlite3.connect(os.path.join(app.root_path, 'music.db')) 
    return g._db_conn

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    if one:
        return rows[0] if rows else None
    else:
        return rows

@app.route("/")
def artists():
    #cur = get_db().cursor()
    #artists = cur.execute("SELECT Name FROM artist LIMIT 10").fetchall()
    artists = query_db("SELECT Name FROM Artist LIMIT 10")
    return render_template("artists.html", artists=artists)

@app.teardown_appcontext
def close_db(exception):
    if "_db_conn" in g:
        g._db_conn.close()
        
conn.close()
