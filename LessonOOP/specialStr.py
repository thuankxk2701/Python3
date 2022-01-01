class Student(object):
    def __init__(self,name):
        self.name=name;
    def __repr__(self):
        return 'Student object (name:%s)'% self.name;
   # __repr__=__str__;
   # Or __str__=__repr__;
s=Student('John')
print(s)