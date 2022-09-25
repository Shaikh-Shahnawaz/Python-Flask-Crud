from app import app
from model.user_model import user_model
from flask import request
# calling class here
obj = user_model()

@app.route("/user/signup/<string:str>")   

def signUp(str):
    # return "Successful Signup !"
    return obj.user_signup_model(str)

@app.route("/users/getusers")

def getAllUsersData():
    return obj.userGetAllData()

@app.route("/users/adduser",methods = ['POST'])
def addUserData():
    data = request.json
    # print('data added',data) 

    return obj.userAddData(data)