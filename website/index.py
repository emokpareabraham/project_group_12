from flask import Flask, render_template, request, g
import sqlite3
import os
import datetime


#print(os.getcwd())

app=Flask(__name__,static_folder='assets')

def to_int(value):
    return int(value)

app.jinja_env.filters['to_int'] = to_int

PER_PAGE = 10

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    page = request.args.get('page', 1, type=int)
    PER_PAGE = request.args.get('per_page',10, type=int)
    start = (page - 1) * PER_PAGE

    end = start + PER_PAGE

    print(start, end)

    con = sqlite3.connect(r'database\Football.db')
    cursor = con.cursor()
    players = cursor.execute(f"SELECT * FROM players limit {start}, {PER_PAGE}").fetchall()
    total_number = cursor.execute("SELECT COUNT(*) FROM players").fetchone()[0]
    con.close()

    g.per_page = PER_PAGE
    g.start = start
    g.end = end
    g.page = page
    g.current_year = datetime.datetime.now().year
    return render_template('data.html', players=players, total_number = total_number)


if __name__=="__main__":
    app.run(debug=True)






