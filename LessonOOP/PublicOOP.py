# program to illustrate public access modifier in a class

class Geek:

    # constructor constructor in the java and javascript
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function  maybe convert self = cls;
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()
