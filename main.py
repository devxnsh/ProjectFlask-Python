from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask('__name__')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120),unique=True, nullable = False)
    datetimer=db.Column(db.DateTime)

    def __repr__(self):
        return f'{self.id} - {self.username} - {self.email} - {self.datetimer}'

def dataentry(Identity, UserID, ElectronicMail,Dated=datetime.utcnow()):
    db.session.add(User(id=Identity, username= UserID, email = ElectronicMail,datetimer=Dated))
    db.session.commit()

@app.route("/")
def home():
    return render_template('index.html')
    #renders the provided html file

@app.route("/about")
def about():
    return "Under Development"
@app.route("/form")
def form():
    return render_template('import.html')

@app.route('/addRegion', methods=['POST'])
def addRegion():
    full = request.form['projectFilePath']
    ment = request.form['email1']
    fill = request.form['username1']
    # dud = request.form['datetime1']
    dataentry(full,fill,ment)
    tester=User.query.filter_by(id=full).first()

    return render_template('regionaloutput.html', alltogether=tester)
@app.route('/data')
def data():
    alltogether=User.query.all() 

    return render_template('output.html', alltogether=alltogether)

if __name__== '__main__':
    app.run(debug=True)