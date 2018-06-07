class User_request():
    
    def __init__(self):
        self.details = [{'id':1,'name':'PITT','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
                        {'id':2,'name':'Alex','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
                       ]
        
    def create_request(self, id, name, dop, top, item_requested_for):
        new_request={'id':id,'name':name,'dop':dop,'top':top,'item requested for':item_requested_for}
        if new_request['id']=="" or new_request['name']=="" or new_request['dop']=="" or new_request['top']=="" or new_request['item requested for']=="":
            return {'message':'All fields are to be filled'}
        self.details.append(new_request)
        return 'Request added'
        

    def get_requests(self):

        return self.details

    def get_request_for_one_user(self, id):
        for detail in self.details:
            if detail['id'] == id:
                return detail
        else:
            return ('request for id %s does not exist') %id

    def update_request(self, name, new_name):
       for detail in self.details:
            if detail['name'] == name:
                detail['name'] = new_name
                return detail
 
 
