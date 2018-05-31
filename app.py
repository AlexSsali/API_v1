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

    

if __name__=="__main__":
    app.run(debug=True)