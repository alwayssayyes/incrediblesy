from flask import render_template, Flask, request, redirect
from app import app
import urllib
from bs4 import BeautifulSoup


@app.route('/')
def test():
	return render_template('getpost.html')

@app.route('/index')
def index():
	return render_template('index.html')
# @app.route('/getpost', methods=['GET', 'POST'])
# def getpost():

# 	get=None
# 	post=None

# 	if request.args:
# 		get = request.args.get['getget']

# 	if request.form:
# 		post = request.form['postpost']

#     return render_template('getpost.html', 
#     	get_variable = get, post_variable = post) 
#     	)

# @app.route('/crawl', methods=['GET','POST'])
# def crawl():
	
# 	if request.method == 'POST' and request.form:
# 		address = request.form.get('crawl')
# 		htmltext = urllib.urlopen(address).read()
# 		soup = BeautifulSoup(htmltext, from_encoding="utf-8")
# 		result=[]
# 		for tag in soup.select(".title"):
# 			result.append(tag.get_text())
# 		return render_template('getpost.html', result=result)
	
# 	else:
# 		return render_template('getpost.html')

@app.route('/yeahyeah')
def ohyeah():
	return render_template('iamsoyoung.html')






# @app.route('/getpost',methods=['GET','POST'])
# def getpost():
#    get_value=None

#    if request.method=='GET':
#       if 'getget' in request.args:
#          get_value=request.args.get('getget')
#          if get_value != 'http://pgr21.com/pb/pb.php?id=freedom':
#             return render_template('listshow.html',error='URL not found')   
#          htmltext = urllib.urlopen(get_value).read()
#          soup = BeautifulSoup(htmltext, from_encoding="utf-8")
#          authors = []
#          for tag in soup.select(".tdname"):
#             authors.append(tag.get_text())
#          return render_template('listshow.html',
#                list=authors)
#       return render_template('getpost.html')


# @app.route('/getpost2',methods=['GET','POST'])
# def getpost2():
#    get_value=None

#    if request.method=='POST':
#       if request.form and ('postpost' in request.form):
#          get_value=request.form['postpost']
#          htmltext = urllib.urlopen(get_value).read()
#          soup = BeautifulSoup(htmltext, from_encoding="utf-8")
#          authors = []
#          for tag in soup.select(".tdname"):
#             authors.append(tag.get_text())
#          return render_template('listshow.html',
#                list=authors)
#       return render_template('getpost.html')


