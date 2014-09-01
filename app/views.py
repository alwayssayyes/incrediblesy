from flask import render_template, Flask, request, redirect, url_for, current_app
from app import app
from urllib2 import urlopen
from bs4 import BeautifulSoup

from flaskext import wtf
from flaskext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError
from google.appengine.ext import db
from database import Member


class Photo(db.Model):
    photo = db.BlobProperty()

class Tweet(db.Model):
    photo = db.BlobProperty()
    text = db.StringProperty()

class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    email = TextField(
        "Email", [validators.Required("Please enter your email address."), validators.Email("Please enter valid email address.")])
    subject = TextField(
        "Subject", [validators.Required("Please enter a subject.")])
    message = TextAreaField(
        "Message", [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")




@app.route('/', methods=["GET", "POST"])
def main():
    form = None
    return render_template('photo.html', form=form)
    
@app.route('/tweet', methods=["GET", "POST"])
def tweet():
    if request.method == 'POST':

        post_data = request.files.get('photo')
        filestream = post_data.read()
        post_dataa = request.form.get('text')
        upload_data = Tweet()
        upload_data.photo = db.Blob(filestream)
        upload_data.text = post_dataa
        upload_data.put()
        datalist=Tweet.all()

        url = url_for("shows", key=upload_data.key())

        return render_template("photo.html", texta=post_dataa, url=url, Tweet=datalist)

    else:
        return render_template('photo.html')

@app.route('/upload', methods=["GET", "POST"])
def upload_db():
    if request.method == 'POST':
        post_data = request.files.get('photo')
        filestream =post_data.read()
        upload_data =Photo()
        upload_data.photo =db.Blob(filestream)
        upload_data.put()
        url = url_for("shows", key=upload_data.key())

        return render_template("photo.html", url=url)
    else:
        return render_template('photo.html')



        
@app.route('/show/<key>', methods=['GET'])
def shows(key):
    uploaded_data = db.get(key)
    return current_app.response_class(
        uploaded_data.photo)

    

@app.route('/vali', methods=["GET", "POST"])
def vali():
    form = ContactForm()
    if request.method == 'POST':
        if not form.validate():
            return render_template('vali.html', form=form)
        else:
            return "Nice to meet you," + form.name.data + "!"
    return render_template('vali.html', form=form)


# class news(Form):
#     category = TextField("category", [validators.Required("Please enter another one")])
#     submit = SubmitField("Send")

# @app.route('/crawlhw', methods=["GET", "POST"])
# def crawlhw():
#     form = news()
#     if request.method == 'POST':
#         if not form.validate():
#             return render_template('crawlhomework.html' )


# @app.route('/lotto', methods=['GET'])
# def lotto():
#     if request.method == 'GET':
#         if request.args.get('getlotto'):
#             html = urlopen(
#                 'http://www.nlotto.co.kr/lotto645Confirm.do?method=allWin').read()
#             bs = BeautifulSoup(html)
#             trs = bs.select('.tblType1 > tbody > tr')
#             lottos = []
#             for i in trs:
#                 tds = i.select('td')
#                 if len(tds) > 1:
#                     lotto = str(i.select('td')[1].get_text())
#                     lotto = lotto.split(', ')
#                     lottos.append(lotto)
#             return render_template('haha.html', lottos=lotto)
#         return render_template('haha.html')

# @app.route('/uploaddb', methods=['GET'])
# def uploaddb():
#     return 0
# # @app.route('/')
# # def test():
# #     return render_template('getpost.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')


# @app.route('/gugu', methods=['get'])
# def gugu():
#     if request.method == 'GET':

#         danstart = request.args.get('danstart')
#         danend = request.args.get('danend')

#         if danstart and danend:
#             gugudan = []
#             for dan in range(int(danstart), int(danend) + 1):
#                 for i in range(1, 10):
#                     gugudan.append(
#                         str(dan) + "x" + str(i) + "=" + str(dan + i))
#             return render_template('haha.html', gugudan=gugudan)
#     return render_template('haha.html')


# @app.route('/cal', methods=['GET', 'POST'])
# def cal():
#     if request.method == 'POST':
#         x = request.form.get('x')
#         op = request.form.get('op')
#         y = request.form.get('y')
#         if x and op and y:
#             result = 0
#             if op == '+':
#                 result = int(x) + int(y)
#                 return render_template('haha.html', calresult=result)
#             elif op == '-':
#                 result = int(x) - int(y)
#                 return render_template('haha.html', calresult=result)
#             elif op == '*':
#                 result = int(x) * int(y)
#                 return render_template('haha.html', calresult=result)
#             elif op == '/':
#                 result = float(x) / float(y)
#                 return render_template('haha.html', calresult=result)
#     return render_template('haha.html')

# @app.route('/what', methods=['GET'])
# def what():
#     if request.method == 'GET':
#         if request.args.get('news'):
#             pass


# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template("photo.html")

# @app.route('/practice', methods=["GET", "POST"])
# def practice():
#     if request.method == 'POST':

#         post_data = request.files.get('photo')
#         filestream = post_data.read()
#         post_dataa = request.form.get('text')
#         upload_data = Database()
#         upload_data.photo = db.Blob(filestream)
#         upload_data.text = post_dataa
#         upload_data.put()
#         datalist=Database.all()

#         url = url_for("shows", key=upload_data.key())

#         return render_template("photo.html", texta=post_dataa, Database=datalist)

#     else:
#         return render_template('photo.html')


# @app.route('/show/<key>', methods=['GET'])
# def shows(key):
#     uploaded_data = db.get(key)
#     return current_app.response_class(
#         uploaded_data.photo)

# @app.route('/', methods=['GET','POST'])
# def show_entries():
#     members = Member.all()
#     return render_template("practice.html", members=members)

# @app.route('/add_entry', methods=['POST'])
# def add_entry():
#     userId = request.form['id']
#     userPasswd = request.form['passwd']

#     for member in Member.all():
#         if userId == member.getId():
#             return "failed"

#     member = Member(userId=userId, userPasswd=userPasswd)
#     member.put()
#     return "OK"



# @app.route('/getpost', methods=['GET', 'POST'])
# def getpost():

#     get=None
#     post=None

#     if request.args:
#     get = request.args.get['getget']

#     if request.form:
#     post = request.form['postpost']

#     return render_template('getpost.html',
#     get_variable = get, post_variable = post)
#     )

# @app.route('/crawl', methods=['GET','POST'])
# def crawl():

#     if request.method == 'POST' and request.form:
#         address = request.form.get('crawl')
#         htmltext = urllib.urlopen(address).read()
#         soup = BeautifulSoup(htmltext, from_encoding="utf-8")
#         result=[]
#         for tag in soup.select(".title"):
#         result.append(tag.get_text())
#         return render_template('getpost.html', result=result)

#     else:
#     return render_template('getpost.html')


# @app.route('/yeahyeah')
# def ohyeah():
#     return render_template('iamsoyoung.html')






# @app.route('/getpost',methods=['GET','POST'])
# def getpost():
# get_value=None

# if request.method=='GET':
# if 'getget' in request.args:
# get_value=request.args.get('getget')
# if get_value != 'http://pgr21.com/pb/pb.php?id=freedom':
# return render_template('listshow.html',error='URL not found')
# htmltext = urllib.urlopen(get_value).read()
# soup = BeautifulSoup(htmltext, from_encoding="utf-8")
# authors = []
# for tag in soup.select(".tdname"):
# authors.append(tag.get_text())
# return render_template('listshow.html',
# list=authors)
# return render_template('getpost.html')


# @app.route('/getpost2',methods=['GET','POST'])
# def getpost2():
# get_value=None

# if request.method=='POST':
# if request.form and ('postpost' in request.form):
# get_value=request.form['postpost']
# htmltext = urllib.urlopen(get_value).read()
# soup = BeautifulSoup(htmltext, from_encoding="utf-8")
# authors = []
# for tag in soup.select(".tdname"):
# authors.append(tag.get_text())
# return render_template('listshow.html',
# list=authors)
# return render_template('getpost.html')