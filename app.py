from flask import Flask, jsonify, request
app = Flask(__name__)
details=[{'id':'1','name':'Alex','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
        {'id':'2','name':'Peter','dop':'18/06/18','top':'14:00','item requested for':'brakes'},
        {'id':'3','name':'Denis','dop':'17/06/18','top':'13:40','item requested for':'engine'}]



@app.route('/api/v1/request/', methods=['GET'])
def _get_details():
    return jsonify(details)


@app.route('/api/v1/request', methods=['POST'])
def create_item():
    detail = request.get_json()  
    details.append(detail)
    return jsonify(message = 'Request added'), 200 

@app.route('/api/v1/request', methods=['PUT'])
def update_item():
    detail= request.get_json()
    name = request.json.get('name', details[0]['name'])
    value = request.json.get('value', details[0]['value'])
    item[0]['name'] = name
    item[0]['value'] = value
    return jsonify({'details': item[0]}), 200

@app.route('/api/v1/request/<string:name>', methods=['PUT'])
def update_item(name):
    #assign all data to detail
    detail= request.get_json()
    #validate
    #if
    #work on data
    detail=[detail for detail in details if detail['name']==name]
    detail[0]['name']=request.json['name']
    return jsonify({'details': detail[0]}), 200
    

if __name__=="__main__":
    app.run(debug=True)