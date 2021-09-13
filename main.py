from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app= Flask('__name__')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120),unique=True, nullable = False)

    def __repr__(self):
        return f'{self.id} - {self.username} - {self.email}'

def datataker():
    idcard = int(input("Enter ID "))
    usernamed = input("Select Username ")
    emailed = input("Enter email ")
    value = User(id=idcard, username = usernamed, email=emailed)
    db.session.add(value)
    db.session.commit()

def dataentry(Identity, UserID, ElectronicMail):
    db.session.add(User(id=Identity, username= UserID, email = ElectronicMail))
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
    dataentry(full,fill,ment)
    fullfillment = (full+"\n" + fill+"\n" +ment)
    alltogether=User.query.all()
    return render_template('output.html', alltogether=alltogether)

if __name__== '__main__':
    app.run(debug=True)