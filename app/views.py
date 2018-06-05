from flask import Flask, jsonify, request
from app import app
import json
from .models import User_request

user_request = User_request()

#get all requests for all users
@app.route('/api/v1/request/', methods=['GET'])
def _get_details():
    requests = user_request.get_requests()
    return jsonify(requests), 200

#get all requests for one user
@app.route('/api/v1/request/<int:id>', methods=['GET'])
def user_detail(id):
    single_request = user_request.get_request_for_one_user(id)
    return jsonify (single_request), 200

#create request
@app.route('/api/v1/request/create', methods=['POST'])
def create_item():
    create = request.get_json()
    create = user_request.create_request(create['id'],create['name'],create['dop'],create['top'],create['item requested for'])
    return jsonify(create)
    return jsonify(message = 'Request added'), 201

#update 
@app.route('/api/v1/request/update/<string:name>', methods=['PUT'])
def update_item(name):
    modify = request.get_json()
    modified = user_request.update_request(modify['name'])
    return jsonify({'details': modified}), 200
    return jsonify(message = 'name updated')
    


  
    
