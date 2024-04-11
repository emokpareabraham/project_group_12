from flask import Flask, render_template
import sqlite3
import os
import datetime


#print(os.getcwd())

app=Flask(__name__,static_folder='assets')

def to_int(value):
    return int(value)

app.jinja_env.filters['to_int'] = to_int

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    print(os.getcwd())
    con = sqlite3.connect(r'database\Football.db')
    cursor = con.cursor()
    players = cursor.execute("SELECT * FROM players limit 10").fetchall()
    con.close()

    current_year = datetime.datetime.now().year
    print(players)
    return render_template('data.html', players=players, current_year = current_year)


if __name__=="__main__":
    app.run(debug=True)






