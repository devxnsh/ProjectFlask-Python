from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120),unique=True, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username
        
def datataker():
    
    idcard = int(input("Enter ID "))
    usernamed = input("Select Username ")
    emailed = input("Enter email ")
    value = User(id=idcard, username = usernamed, email=emailed)

    db.session.add(value)
    db.session.commit()
def dataentry(Identity, UserID, ElectronicMail):
    from SQLAT import db, User
    
    value=User(id=Identity, username= UserID, email = ElectronicMail)
    db.session.add(value)
    db.session.commit()
if __name__=='__main__':
    datataker()