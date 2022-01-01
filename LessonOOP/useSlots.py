
class Student(object):
    __slots__ = ('name', 'age') ;
class GraduateStudent(Student):
    pass;

s = Student() 
s.name = 'Michael';
s.age = 25;
# ERROR: AttributeError: 'Student' object has no attribute 'score'
print(f'Name is {s.name} age {s.age}');
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)