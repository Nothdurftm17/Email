from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.email import Email
#======================================================
#ROUTE RENDERS TO HOME PAGE
@app.route('/')
def index():

    return render_template('index.html')
#======================================================

#======================================================
#ROUTE THAT PROCESSES "POST" TO VALIDATE/ CREATE EMAIL 
@app.route('/addEmail', methods=['POST'])
def addEmail():

    session['email_address'] = request.form['email_address']

    if Email.is_valid(request.form):
        Email.save(request.form)
        return redirect ('/emails')
    
    return redirect('/')
#======================================================

#======================================================
#ROUTE RENDERS TO SECOND PAGE
@app.route('/emails')
def emails():
    
    return render_template('second.html', allEmails = Email.allEmails())
#======================================================
#======================================================
#ROUTE PROCESSES DELETE
@app.route('/emails/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }
    Email.delete(data)
    return redirect('/emails')