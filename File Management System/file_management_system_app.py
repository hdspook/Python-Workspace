import os
from flask import Flask 
from flask_restful import reqparse, Resource, Api
from flask_sqlalchemy import SQLAlchemy
#from entity.patients import Patients,db
from utility.file_check import fileIsPresent
from utility.read_file import readFile
from handlers.converter_handler import convert_data_xlsx, docx_to_pdf, xlsx_to_pdf
from handlers.merge_handler import merge_pdfs

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
'''
    Accepts a file name as post requests
    url = "http://127.0.0.1:5000/retrieve" 
    x = requests.post(url, data = {'file' : 'test.txt'})
'''
class RetrieveAndSave(Resource):

    def post(self):
        args = parser.parse_args()
        file_name = os.path.abspath(args['file'])
        #Search for file
        app.logger.info("Searching For File")
        if fileIsPresent(file_name):
            #read data from file
            line = readFile(file_name).split(",")
            #Save data to database
            details = Patients(id=int(line[0]), name=line[1], email=line[2])
            db.session.add(details)
            db.session.commit()
            app.logger.info(Patients.query.all())
            #Convert the data to xlsx
            convert_data_xlsx(file_name)
            return "successful()"
        
        else:
            app.logger.info("File Not Present")
            return "unsuccessful()"

#Endpoint to convert various documents formats to pdf
'''
    Accepts a file name as post requests
    url = "http://127.0.0.1:5000/convert" 
    x = requests.post(url, data = {'file' : 'test.txt'})
'''
class Converter(Resource):

    def post(self):
        args = parser.parse_args()
        file_name = os.path.abspath(args['file'])
        app.logger.info(file_name)
        #Search for file
        app.logger.info("Searching For File")
        if fileIsPresent(file_name):
            #Check for file format(.docx, .xlsx)
            if file_name.endswith(".docx"):
                docx_to_pdf(file_name)

            elif file_name.endswith(".xlsx"):
                xlsx_to_pdf(file_name)

            else:
                app.logger.info("File Format Not Applicable")
                return "unsuccessful()"
        
        else:
            app.logger.info("File Not Present In Current Path")
            return "unsuccessful()"
        
        return" successful()"

#Endpoint to merge multiple pdf files
'''
    Accepts a list of pdfs as post requests
    url = "http://127.0.0.1:5000/merge" 
    x = requests.post(url, data = {'file' : 'Dummy.pdf,b_2.pdf'})
'''
class Merger(Resource):

    def post(self):
        args = parser.parse_args()
        file_list_received = args['file'].split(",")
        updated_file_list = [os.path.abspath(file.strip()) for file in file_list_received]
        app.logger.info(updated_file_list)
        #Call Merge Function
        merge_pdfs(updated_file_list)
        return "successful()"


##
## Actual setup the Api resource routing here
##
api.add_resource(RetrieveAndSave, '/retrieve')
api.add_resource(Converter, '/convert')
api.add_resource(Merger, '/merge')

#Driver
if __name__ == "__main__":
    db.drop_all() 
    db.create_all() 
    app.run(debug = True)