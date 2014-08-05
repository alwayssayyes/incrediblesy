from google.appengine.ext import db

class Database(db.Model):
    photo = db.BlobProperty()
    text = db.StringProperty()


class Member(db.Model):
	userId = db.StringProperty()
	userPasswd = db.StringProperty()

	def getId(self):
		return self.userId

	def getPasswd(self):
		return self.userPasswd

	def setId(self):
		self.userId = userId

	def setPasswd(self):
		self.userPasswd = userPasswd

	def getInfo(self):
		result = {}
		result['userId']= self.getId()
		result['userPasswd']= self.getPasswd()
		return result