import unittest
import flask, json
from app import app

class MyApi(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        self.dummy = [{'id':1,'name':'Alex','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
        {'id':2,'name':'Peter','dop':'18/06/18','top':'14:00','item requested for':'brakes'},
        {'id':3,'name':'Denis','dop':'17/06/18','top':'13:40','item requested for':'engine'}]

    def test_get_request(self):
        response = self.tester.get("/api/v1/request/", 
                                content_type="application/json",
        data=json.dumps(self.dummy))
        responsejson = json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)

    

    def test_get_request_for_one_user(self):
        response = self.tester.get("/api/v1/request/1", 
                                content_type="application/json",
        data=json.dumps(self.dummy))
        responsejson = json.loads(response.data.decode())
        self.assertEqual("Alex", responsejson['details']["name"])
        self.assertEqual(response.status_code,200)

    
    def test_for_update(self):
        response = self.tester.put("/api/v1/request/update/Peter", 
                                content_type="application/json",
        data=json.dumps({"name": "Juliuss"}))
        responsejson = json.loads(response.data.decode())
        self.assertEqual("Juliuss", responsejson['details']["name"])
        self.assertEqual(response.status_code,200)

    def test_for_create_request(self):
        response = self.tester.post("/api/v1/request/create",content_type="application/json",
        data = json.dumps({
        "dop": "17/06/18",
        "id": 4,
        "item requested for": "tyre",
        "name": "Joe",
        "top": "13:30"}))
        responsejson = json.loads(response.data.decode())
        self.assertEqual(response.status_code,201)
        self.assertEqual(responsejson['message'],"Request added")


if __name__ == "__main__":
    unittest.main()
