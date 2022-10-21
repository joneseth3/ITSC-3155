import os                 
from flask import Flask   
from flask import render_template
from flask import request


app = Flask(__name__)     # create an app



@app.route('/index')
def index():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}

    return render_template('index.html', user = a_user)



@app.route('/notes')
def get_notes():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}
    notes = {1: {'title': 'First note', 'text': 'this is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second note', 'text': 'this is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third note', 'text': 'this is my third note', 'date': '10-17-2020'}
            }

    return render_template('notes.html', notes = notes, user = a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}
    notes = {1: {'title': 'First note', 'text': 'this is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second note', 'text': 'this is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third note', 'text': 'this is my third note', 'date': '10-17-2020'}
            }

    return render_template('note.html', note = notes[int(note_id)], user = a_user)

@app.route('/notes/new', methods=['GET','POST'])
def new_note():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}

    print('request method is', request.method)
    if request.method == 'POST':
        request_data = request.form
        return f"data: {request_data} !"
    else:
        return render_template('new.html', user = a_user)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)
