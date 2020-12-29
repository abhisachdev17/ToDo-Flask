from flask import Flask, render_template, request, Response, jsonify
import json
import db_utils

TODO = 'To do'
COMPLETED = 'Completed'

app = Flask(__name__)

db_utils.db_init()

# the first route you will visit
@app.route('/')
def index():
    return 'Hello World!'

# the endpoint to add the items
@app.route('/item/add', methods= ['POST'])
def addToDo():

    # get the item from the body
    data = request.get_json()
    item = data['item']

    print(item)
    response = db_utils.add_item(item, TODO)
    if response is None:
        return Response("{'error': Item not added}", status=500, mimetype= 'application/json')
    
    return jsonify(response)
