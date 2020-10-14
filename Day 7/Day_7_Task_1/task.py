from flask import Flask, request, jsonify
app = Flask(__name__)

name = ["Himanshu"]

@app.route('/getname')
def getname():
    return jsonify( 
          
          {"name " : name[0]}
          
          ) if len(name) != 0 else jsonify( 
          
          {"LIST_STATUS" : "empty"}
          
          )

@app.route('/success',methods = ['POST', 'GET', 'PUT','DELETE'])
def success():
    if request.method == 'POST':
        user = request.form['name']
        return jsonify( 
          
          {"Hello " : user}
          
          )
    elif request.method == 'PUT':
        user = request.form['name']
        name[0] = user
        return jsonify( 
          
          {"Update_Status" : "Success"}
          
          )
    elif request.method == 'DELETE':
        del name[0]
        return jsonify( 
          
          {"DELETE_Status" : "Success"}
          
          )
    
    else:
        return jsonify( 
          
          {"Hello " : "World"}
          
          ) 

if __name__ == '__main__':
   app.run(debug = True)