import json;
d=dict(name="KeyXK",age=19,score=88);
data=json.dumps(d);
# print('JSON Data is a str:', data);
reborn=json.loads(data);
# print(reborn);

class Student(object):
    def __init__(self,name,age,score):
        self.name=name;
        self.age=age;
        self.score=score;
    def __str__(self):
         return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score);
s = Student('keyXK', 19, 88);
print(s);
stdData=json.dumps(s,default=lambda obj:obj.__dict__);

print('Dump Student:', stdData);
rebuild = json.loads(stdData, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)