from flask import Flask, jsonify, request
app = Flask(__name__)
details=[{'id':1,'name':'Alex','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
        {'id':2,'name':'Peter','dop':'18/06/18','top':'14:00','item requested for':'brakes'},
        {'id':3,'name':'Denis','dop':'17/06/18','top':'13:40','item requested for':'engine'}]


#get all requests for all users
@app.route('/api/v1/request/', methods=['GET'])
def _get_details():
    return jsonify(details), 200

#get all requests for one user
@app.route('/api/v1/request/<int:id>', methods=['GET'])
def user_detail(id):
    detail=[detail for detail in details if detail['id'] == id]
    return jsonify ({'details': detail[0]}), 200

#create request
@app.route('/api/v1/request/create', methods=['POST'])
def create_item():
    detail = request.get_json()  
    details.append(detail)
    return jsonify(message = 'Request added'), 201

#update 
@app.route('/api/v1/request/update/<string:name>', methods=['PUT'])
def update_item(name):
    detail= request.get_json()
    detail=[detail for detail in details if detail['name']==name]
    detail[0]['name']=request.json['name']
    return jsonify({'details': detail[0]}), 200
    return jsonify(message = 'name updated')
    

if __name__=="__main__":
    app.run(debug=True)