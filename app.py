# import necessary libraries
from flask import Flask

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route('/')
def hello_world():

    return  'Hello World'




