from flask import Flask, render_template ,request
import codecs
import datetime
app = Flask(__name__)

@app.route("/")
def go_index():
    return render_template("index.html")

@app.route("/career.html")
def go_career():
    return render_template("career.html",)

@app.route("/research.html")
def go_research():
    return render_template("research.html",)

@app.route("/skill.html")
def go_skill():
    return render_template("skill.html",)

@app.route("/bbs.html",)
def go_bbs():
    file = codecs.open("web_des_html1/static/article.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    today = datetime.datetime.now()
    date_now = today.strftime("%Y/%m/%d")
    return render_template("bbs.html",lines = lines, date_now=date_now,)

@app.route("/bbs.html/result", methods=["POST"])
def result():
    article = request.form["article"]
    name = request.form["name"]

    file = codecs.open("web_des_html1/static/article.txt", "a", "utf-8")
    file.write(article + "," + name + "\n")
    file.close()
    return render_template("bbs_result.html", article = article, name = name,)