import json
from pprint import  pprint
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.future_me=None
me=user("weidiao",24)
me.future_me=user(me.name,me.age+1)
s=json.dumps(me,default=lambda o:o.__dict__,indent=4)
print(s)
