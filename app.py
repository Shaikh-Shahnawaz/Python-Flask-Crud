import imp
from flask import Flask,jsonify

app = Flask(__name__)


@app.route("/")

def welcome():
    return 'Hello World !'

@app.route("/home/<string:str>")   

def greet(str):
    return f"Welcome Home {str} 😊"


from controller import *
# from controller import user_controller,product_controller   

# import controller.user_controller  as user_controller 