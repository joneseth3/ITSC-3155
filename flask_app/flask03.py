from cgitb import text
import os
from turtle import title
from flask import Flask   
from flask import render_template
from flask import request
from flask import redirect, url_for

app = Flask(__name__)     # create an app


notes = {1: {'title': 'First note', 'text': 'this is my first note', 'date': '10-1-2020'},
         2: {'title': 'Second note', 'text': 'this is my second note', 'date': '10-2-2020'},
         3: {'title': 'Third note', 'text': 'this is my third note', 'date': '10-17-2020'}
        }



@app.route('/index')
def index():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}

    return render_template('index.html', user = a_user)



@app.route('/notes')
def get_notes():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}
  
    return render_template('notes.html', notes = notes, user = a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}

    return render_template('note.html', note = notes[int(note_id)], user = a_user)

@app.route('/notes/new', methods=['GET','POST'])
def new_note():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}

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
        # get the last ID used an increment by 1 
        id = len(notes) +1
        # create new note 
        notes[id] = {'title': title, 'text': text, 'date': today}

        return redirect(url_for('get_notes'))
    else:
        return render_template('new.html', user = a_user)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)
