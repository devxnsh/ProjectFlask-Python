import re
from flask import Flask, render_template,request
app= Flask('__name__')
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
    from SQLAT import dataentry
    dataentry(full,fill,ment)
    fulfilment = (full+"\n" + fill+"\n" +ment)
    return fulfilment
if __name__== '__main__':
    app.run(debug=True)