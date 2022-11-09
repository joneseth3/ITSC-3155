from flask import Flask
from database import db
from cgitb import text
import os
from turtle import title
from flask import Flask   
from flask import render_template
from flask import request
from flask import redirect, url_for
from models import Note as Note
from models import User as User 






app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()   # run under the app context


@app.route('/')
@app.route('/index')
def index():
    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')

    return render_template('index.html', user = a_user)



@app.route('/notes')
def get_notes():
    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
    my_notes = db.session.query(Note).all()

    return render_template('notes.html', notes=my_notes, user=a_user)


@app.route('/notes/<note_id>')
def get_note(note_id):
    a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
    my_note = db.session.query(Note).filter_by(id=note_id).one()

    return render_template('note.html', note = my_note, user = a_user)

@app.route('/notes/new', methods=['GET','POST'])
def new_note():

    #check method 
    if request.method == 'POST':
        # get title 
        title = request.form['title']
        # get note 
        text = request.form['noteText']
        # create time stamp
        from datetime import date 
        today = date.today()
        # format date 
        today = today.strftime("%m-%d-%Y")
        new_record = Note(title,text, today)
        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for('get_notes'))
    else:
        a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')
        return render_template('new.html', user = a_user)




@app.route('/notes/edit/<note_id>', methods=['GET', 'POST'])
def update_note(note_id):
    
    if request.method == 'POST':

        title = request.form['title']

        text = request.form['noteText']
        note = db.session.query(Note).filter_by(id=note_id).one()

        note.title = title
        note.text = text

        db.session.add(note)
        db.session.commit()

        return redirect(url_for('get_notes'))
    else:
    
    
        a_user = db.session.query(User).filter_by(email='mogli@uncc.edu')

        my_note = db.session.query(Note).filter_by(id=note_id).one()

        return render_template('new.html', note=my_note, user=a_user)


@app.route('/notes/delete/<note_id>', methods=['POST'])
def delete_note(note_id):
    my_note = db.session.query(Note).filter_by(id=note_id).one()
    db.session.delete(my_note)
    db.session.commit()

    return redirect(url_for('get_notes'))



app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)