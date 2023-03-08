from flask import Flask, render_template, url_for


app = Flask(__name__)

menu = [{"name": "Первая страница", "url": "page_1"},
        {"name": "Вторая страница", "url": "page_2"},
        {"name": "Третья страница", "url": "page_3"}]


@app.route("/")
@app.route("/page_1")
def page_1():
    return render_template("page_1.html", title="Первая страница", menu=menu)


@app.route("/page_2")
def page_2():
    return render_template("page_2.html", title="Вторая страница", menu=menu)


@app.route("/page_3")
def page_3():
    return render_template("page_3.html", title="Третья страница", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)