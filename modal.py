
from app import db

class Links(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    alias = db.Column(db.String(5), unique = True)
    user_link = db.Column(db.String, nullable= False)
    def __repr__(self):
        #represent alias to prevent duplicate aliases
        return '<Link: {}>'.format(self.user_link)
