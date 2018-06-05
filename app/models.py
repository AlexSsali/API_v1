class User_request():
    
    def __init__(self):
        self.details = [{'id':1,'name':'PITT','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
                        {'id':2,'name':'Alex','dop':'17/06/18','top':'13:00','item requested for':'tyre'},
                       ]
        
    def create_request(self, id, name, dop, top, item_requested_for):
        new_request={'id':id,'name':name,'dop':dop,'top':top,'item requested for':item_requested_for}
        self.details.append(new_request)
        return 'request added'
        

    def get_requests(self):
        return self.details

    def get_request_for_one_user(self, id):
        for detail in self.details:
            if detail['id'] == id:
                return detail
            else:
                return 'request does not exist' 

    def update_request(self, name, new_name):
       for detail in self.details:
            if detail['name'] == name:
                return detail
 
 
