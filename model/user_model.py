import mysql.connector
import json
import config

class user_model():

    # this is constructor function
    def __init__(self):
        try:
            # connections establishment code
            # print("sql credentials",config.mysql_hostname)
            self.con = mysql.connector.connect(
                host=config.mysql_hostname, user=config.mysql_user, password=config.mysql_password, database=config.mysql_database_name)
            self.con.autocommit = True
            # we can write query with the help of cursor and output will be in json format
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("some error")

    def user_signup_model(str):
        # query execution code
        return f"This is Signup Model {str} "

    def userGetAllData(self):
        self.cur.execute("select * from users")
        result = self.cur.fetchall()
        # print('result =>',result)
        # convert data to stringify then send response
        stringifyJson = json.dumps(result)
        return result

    def userAddData(self, data):
        self.cur.execute(
            f"insert into users(name,email,phone,role,password) value('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')"
            )
        return "User created successfully"
