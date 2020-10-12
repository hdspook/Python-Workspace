from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/username/<string:username>')
def hello_user(username):
    return 'Hello ! '+ username

@app.route('/userid/<int:userid>')
def hello_user_id(userid):
    return 'Hello ! '+ str(userid)

@app.route('/json')
def testing_jsonify():
    return jsonify(
        {
            "Author":"Himanshu Dubey"
        }
    )