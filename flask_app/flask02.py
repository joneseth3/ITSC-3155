# imports
import os                 
from flask import Flask   
from flask import render_template


app = Flask(__name__)     # create an app



@app.route('/index')



def index():
    a_user = {'name': 'Seth', 'email':'mogil@uncc.edu'}

    return render_template('index.html', user = a_user)


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)


 
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000
