#!/usr/bin/env python

import json

class Student(object):

    def __init__(self, name, age, score):
        
        self.name = name
        self.age = age 
        self.score = score 

s = Student('Jack', 18, 80)

#def obj2dict(std):
#    return {
#        'name': std.name,
#        'age': std.age,
#        'score': std.score
#    }

#print('json str of object %s' %json.dumps(s, default=obj2dict))
print('json str of object %s' %json.dumps(s, default=lambda obj: obj.__dict__))
