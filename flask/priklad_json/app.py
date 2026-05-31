import os

from flask import Flask, render_template, request, jsonify
import mysql.connector
import json


mydb = mysql.connector.connect(
    host = "dbs.spskladno.cz"
    ,user = "student14"
    ,password = "spsnet"
    ,database = "vyuka14"
)
app = Flask(__name__)


@app.route('/')
def vizitka():  # put application's code here
    print("ahoj")
    with open("profile.json", encoding="utf-8") as f:
        profile = json.load(f)
        #profile['title_before']
    return render_template("lecturer.html", profile=profile)

if __name__ == '__main__':
    app.run()
