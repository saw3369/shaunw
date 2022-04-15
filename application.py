from flask import Flask, redirect, url_for, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/cv/")
def CV():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/assets/'
    return send_from_directory(filepath, 'James Wylde - Escalation Engineer at Microsoft (pic).pdf')

