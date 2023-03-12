import sqlite3
import os
from flask import Flask, render_template, url_for, g
from FDateBase import FDateBase

DATABASE = "/path/HW_flsk.db"
DEBUG = True
SECRET_KEY = "b4d6ad6dc4a0ba3eda5012d214e320c2ae17f5c6"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, "HW_flsk.db"))


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("HW_sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def page_1():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("page_1.html", title="Первая страница", menu=dbase.get_menu())


@app.route("/page_2")
def page_2():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("page_2.html", title="Вторая страница", menu=dbase.get_menu())


@app.route("/page_3")
def page_3():
    db = get_db()
    dbase = FDateBase(db)
    return render_template("page_3.html", title="Третья страница", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link.db"):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Страница не найдена")


if __name__ == "__main__":
    app.run(debug=True)
