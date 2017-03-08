import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required



class Item(Resource):
    # Using reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be blank")

    @jwt_required()
    def get(self, name):
        try:
            item = self.find_by_name(name)
        except:
            return {'message': 'Error retrieving object from database'}, 500
        if item:
            return item
        return {'message': 'Item not found'}, 404

    def post(self, name):
        # Ensure item doesn't already exist
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exist".format(name)}, 400 # 400: Bad request

        data = Item.parser.parse_args()

        item = {'item': name, 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {'message': "An error ocurred inserting the item."}, 500

        return item, 201

    def delete(self,name):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        if self.find_by_name(name):
            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (name,))
        else:
            return {'message': 'Item nonexistent in database'}

        conn.commit()
        conn.close()

        return {'message': 'Item successfully deleted'}, 201


    def put(self, name):
        # Using parser instead of request
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'item': name, 'price': data['price']} # var updated_item used so as not to replace item

        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {'message': 'Error inserting item to database'}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {'message': 'Error updating item in database'}, 500
        return item

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @classmethod
    def insert(cls, item):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['item'], item['price'],))

        conn.commit()
        conn.close()
    @classmethod
    def update(cls, item):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['item'],))

        conn.commit()
        conn.close()


class ItemList(Resource):
    def get(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        items = []

        for row in result:
            items.append({'name': row[0], 'price': row[1]})     #directly from database

        conn.close()

        return {'items': items}