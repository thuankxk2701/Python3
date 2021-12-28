class Student(object):
    def __init__(self,name,score):
        self.name=name;
        self.score=score;
    def getScore(self):
        print('%s: %s' % (self.name, self.score));
    def getGrade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.name="Thuan"
print('bart.name =', bart.name);
print('bart.score =', bart.score);


bart.getScore();

print('grade of Bart:', bart.getGrade())
print('grade of Lisa:', lisa.getGrade())
