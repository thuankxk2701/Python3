class Person:
    count = 0

    def __init__(cls, name: str, age: int):
        cls.name = name
        cls.age = age
        Person.count += 1

    @classmethod
    def show_count(self):

        print(f"Hiện có {self.count} object Person trong chương trình")

putin = Person('Putin Vladimir', 60);
putin.show_count();
trump = Person('Trump Donald', 60)
trump.show_count();
Person.show_count();
