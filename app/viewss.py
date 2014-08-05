from flask import render_template, Flask, request, redirect, url_for, current_app
from app import app
from urllib2 import urlopen
from bs4 import BeautifulSoup
from google.appengine.ext import db
from flaskext import wtf
from flaskext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError
from database import Member

@app.route('/')
@app.route('/index')
def index():
	return render_template("photo.html")

@app.route('/practice', methods=["GET", "POST"])
def practice():
    if request.method == 'POST':

        post_data = request.files.get('photo')
        filestream = post_data.read()
        post_dataa = request.form.get('text')
        upload_data = Database()
        upload_data.photo = db.Blob(filestream)
        upload_data.text = post_dataa
        upload_data.put()
        datalist=Database.all()

        # url = url_for("shows", key=upload_data.key())

        return render_template("photo.html", texta=post_dataa, Database=datalist)

    else:
        return render_template('photo.html')


@app.route('/show/<key>', methods=['GET'])
def shows(key):
    uploaded_data = db.get(key)
    return current_app.response_class(
        uploaded_data.photo)

@app.route('/', methods=['GET','POST'])
def show_entries():
    members = Member.all()
    return render_template("practice.html", members=members)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    userId = request.form['id']
    userPasswd = request.form['passwd']

    for member in Member.all():
        if userId == member.getId():
            return "failed"

    member = Member(userId=userId, userPasswd=userPasswd)
    member.put()
    return "OK"
