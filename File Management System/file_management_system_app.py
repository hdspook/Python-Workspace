from flask import Flask 
from flask_restful import reqparse, Resource, Api
from flask_sqlalchemy import SQLAlchemy
#from entity.patients import Patients,db
from utility.file_check import fileIsPresent
from utility.read_file import readFile

#Initializing the app
app = Flask(__name__)

#Initializing the api
api = Api(app)

#Initializing the request parser
parser = reqparse.RequestParser()
parser.add_argument('file')

#Initializing app for SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

#Model Class
class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Patients %r>' % self.name



#Endpoint to retrieve file data from server and save to database
class RetrieveAndSave(Resource):

    def post(self):
        args = parser.parse_args()
        file_name = args['file']
        #Search for file
        app.logger.info("Searching For File")
        if fileIsPresent(file_name):
            #read data from file
            line = readFile(file_name).split(",")
            #Save data to database
            details = Patients(id=int(line[0]), name=line[1], email=line[2])
            db.session.add(details)
            db.session.commit()
            #Convert the data to xlsx
            
            return "successful()"
        
        else:
            app.logger.info("File Not Present")
            return "unsuccessful()"

##
## Actually setup the Api resource routing here
##
api.add_resource(RetrieveAndSave, '/retrieve')

#Driver
if __name__ == "__main__":
    db.drop_all() 
    db.create_all() 
    app.run(debug = True)