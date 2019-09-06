from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

stores = [
    {
        'name': 'Emag Store',
        'items': [
            {
                'name': 'Item 1',
                'price': 109.99
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store')
def get_stores():
    #return jsonify({'stores':stores})
    return jsonify(stores)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

@app.route('/store/<string:name>/item')
def get_item():
    pass

app.run(port=5000)