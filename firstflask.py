from flask import Flask
from flask_restplus import Resource, Api, fields, reqparse

app = Flask(__name__)
api = Api(app, version='1.0', title='TodoMVC API', description='A simple TodoMVC API', )

ns = api.namespace('todo', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

parser = reqparse.RequestParser()
parser.add_argument('id', type=str, required=True, help="id")
parser.add_argument('name', type=str, required=True, help="名称")
parser.add_argument('volume', type=int, required=True, help="方量")


class TodoDAO(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params = parser.parse_args()

    @ns.expect(parser)
    @ns.response(200, "success response", todo)
    def get(self):
        return self.params


ns.add_resource(TodoDAO, "/to", endpoint="to_do")


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)
