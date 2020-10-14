from flask import Flask, jsonify
from flask_restful import reqparse, Resource, Api
from flask_sqlalchemy import SQLAlchemy

#Initializing the app
app = Flask(__name__)

#Initializing the api
api = Api(app)

#Initializing the request parser
parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('email')

#Initializing app for SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

#Model Class
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f"<Students : {self.id} {self.name} {self.email}>"



#Endpoint to retrieve file data from server and save to database
class StudentsList(Resource):

    def get(self):
        l = Students.query.all()
        app.logger.info(l)
        return "Students.query.all()"

    def post(self):
        args = parser.parse_args()
        app.logger.info(args)
        id = int(args['id'])
        name = args['name']
        email = args['email']
        details = Students(id=id, name=name, email=email)
        db.session.add(details)
        db.session.commit()
        app.logger.info("Students Added Successfully")
        l = Students.query.all()
        app.logger.info(l)
        return "Added Successfully"
    def put(self):
        args = parser.parse_args()
        app.logger.info(args)
        id = int(args['id'])
        name = args['name']
        email = args['email']
        Students.query.filter_by(id = id).update({Students.name:name, Students.email:email})
        db.session.commit()
        app.logger.info("Students Updated Successfully")
        l = Students.query.all()
        app.logger.info(l)
        return "Updated Successfully"

    def delete(self):
        args = parser.parse_args()
        app.logger.info(args)
        id = int(args['id'])
        Students.query.filter_by(id = id).delete()
        db.session.commit()
        app.logger.info("Students Deleted Successfully")
        l = Students.query.all()
        app.logger.info(l)
        return "Deleted Successfully"
##
## Actually setup the Api resource routing here
##
api.add_resource(StudentsList, '/students')

#Driver
if __name__ == "__main__":
    db.drop_all() 
    db.create_all() 
    app.run(debug = True)