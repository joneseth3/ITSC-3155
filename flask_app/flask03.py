import os                 
from flask import Flask   
from flask import render_template


app = Flask(__name__)     # create an app



@app.route('/index')
def index():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}

    return render_template('index.html', user = a_user)



@app.route('/notes')
def get_notes():
    notes = {1: {'title': 'First note', 'text': 'this is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second note', 'text': 'this is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third note', 'text': 'this is my third note', 'date': '10-17-2020'}
            }

    return render_template('notes.html', notes = notes)

@app.route('/notes/<note_id>')
def get_note(note_id):
    notes = {1: {'title': 'First note', 'text': 'this is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second note', 'text': 'this is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third note', 'text': 'this is my third note', 'date': '10-17-2020'}
            }

    return render_template('note.html', note = notes[int(note_id)])

@app.route('/notes/new')
def new_note():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}
    return render_template('new.html', user = a_user)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)
