import unittest
import flask, json
from app import app

class MyApi(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_get_request(self):
        
        #variable called response, calls self.tester with GET method and hands over 
        #content/paylod otained from /api/v1.... url with json content type
        response = self.tester.get("/api/v1/request/", 
                                content_type="application/json",
        #json.dump looks for all data with tied with Alex value and sends it in encoded
        #form
        data=json.dumps(dict(name="Alex")))
        #json.load function receives and decodes it then assigns it to responsejson
        responsejson = json.loads(response.data.decode())
        ##check if value Alex in position[0] with key name while
        self.assertEqual("Alex", responsejson[0]["name"])
        #checking if status code recieved is 200
        self.assertEqual(response.status_code,200)

    


if __name__ == "__main__":
    unittest.main()
