from flask import Flask
from flask_restful import abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TASKS = {
    'task1': {'task': 'Develop Frontend'},
    'task2': {'task': 'Develop Backend'},
    'task3': {'task': 'Do Testing'},
}

DEVELOPERS = {
    '1': {"task1" : "Himanshu Dubey"},
    '2': {"task2" : "Akash"},
    '3': {"task3" : "Vamsi"},
}


def check(id, items):
    if id not in items:
        abort(404, message="{} doesn't exist".format(id))

def get_developers_list(item):
    DEVELOPERS_LIST = {}
    for id, developer in DEVELOPERS.items():
        for _ , name in developer.items():
            DEVELOPERS_LIST[id] = name
    return DEVELOPERS_LIST

# DevelopersList
# shows a list of all Developers
class DevelopersList(Resource):
    def get(self):
        return get_developers_list(DEVELOPERS)

class Developer(Resource):
    def get(self, id):
        developers_list = get_developers_list(DEVELOPERS)
        check(id, developers_list)
        return developers_list[id]

class DeveloperTask(Resource):
    def get(self, id):
        check(id, DEVELOPERS)
        developer_task = DEVELOPERS[id]
        key = [key for key,_ in developer_task.items()]
        return TASKS[key[0]]



##
## Actually setup the Api resource routing here
##
api.add_resource(DevelopersList, '/developers', '/')
api.add_resource(Developer, '/developers/<id>')
api.add_resource(DeveloperTask, '/developers/<id>/tasks')


if __name__ == '__main__':
    app.run(debug=True)