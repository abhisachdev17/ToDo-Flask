from flask import Flask, render_template, request, Response, jsonify
import json
import db_utils

TODO = 'to do'
COMPLETED = 'completed'

app = Flask(__name__)

db_utils.db_init()

# the first route you will visit
@app.route('/')
def index():
    return 'Hello World!'

# the endpoint to add the items
@app.route('/item/add', methods= ['POST'])
def add_ToDo():

    # get the item from the body
    data = request.get_json()
    item = data['item']

    print(item)
    response = db_utils.add_item(item, TODO)
    if response is None:
        return Response("{'error': Item not added}", status=500, mimetype= 'application/json')
    
    return jsonify(response)

# retrieve all items 
@app.route('/items')
def get_all_ToDos():
    return db_utils.get_all_items()

# retrieve a single item from the db by its key
@app.route('/item', methods=['GET'])
def get_item():

    key = request.args.get('key')
    print(key)

    item = db_utils.get_item(key)

    if item is None:
        return Response("{'error': 'Item not found'}", status=404, mimetype='application/json')
    
    return jsonify(item)

# update status of an item
@app.route('/item/update', methods=['PUT'])
def update_status():
    data = request.get_json()
    key = data['key']
    status = data['status']
    
    status = status.lower().strip()
    print(status)
    
    response = None

    if (status == TODO or status == COMPLETED):
        print('updating item..')
        response = db_utils.update_item(key, status)
    
    if response is None:
        return Response("{'error': Item not Updated}", status=304, mimetype= 'application/json')
    
    return jsonify(response)