from flask import Flask, jsonify, request
app = Flask(__name__)
details=[{'id':'1','name':'Alex','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
        {'id':'2','name':'Peter','dop':'18/06/18','top':'14:00','item requested for':'brakes'},
        {'id':'3','name':'Denis','dop':'17/06/18','top':'13:40','item requested for':'engine'}]

# def get_request_details(name):
#     return [details for details in details if details["name"] == name]
# def _get_details(id):
#     return [details for details in details if details['id'] == id]
# def length():
#     return len(details)

@app.route('/api/v1/request/', methods=['GET'])
def _get_details():
    return jsonify(details)


@app.route('/api/v1/request', methods=['POST'])
def create_item():
    detail = request.get_json()  
    details.append(detail)
    return jsonify(message = 'Request added'), 200

# @app.route('/api/v1/request/<int:id>', methods=['PUT'])
# def update_item(id):
#     name = request.json.get('name', details[0]['name'])
#     value = request.json.get('value', details[0]['value'])  
#     details[0]['name'] = name
#     details[0]['value'] = value
#     return jsonify({'item': details[0]}), 200
 

    

if __name__=="__main__":
    app.run(debug=True)