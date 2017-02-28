# Using Flask-RESTful so no need to use jsonify!
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'fomenky'
api = Api(app)

jwt = JWT(app, authenticate, identity)      # /auth

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(iter(filter(lambda l: l['item'] == name, items)), None) # next returns the next item in the filter list
        return {'item': item}, 200 if item is not None else 404             # 404: Resource not found

    def post(self, name):
        # Ensure item doesn't already exist
        if next(iter(filter(lambda l: l['item'] == name, items)), None):
            return {'message': "An item with name '{}' already exist".format(name)}, 400 # 400: Bad request

        request_data = request.get_json()
        item = {'item': name, 'price': request_data['price']}
        items.append(item)

        print item

        return item, 201

    def delete(self,name):
        global items
        if next(iter(filter(lambda l: l['item'] == name, items)), None):
            items = list(filter(lambda l: l['item'] != name, items))
            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 400

    def put(self, name):
        # Using parser instead of request
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True, help="This field cannot be blank")

        request_data = parser.parse_args()
        item = next(iter(filter(lambda l: l['item'] == name, items)), None)
        if item is None:
            item = {'item': name, 'price': request_data['price']}
            items.append(item)
        else:
            item.update(request_data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')  #Ex: http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)


