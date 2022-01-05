class Node:
    def __init__(self,init_data):
        self.data=init_data;
        self.next=Node;
    def getData(self):
        return self.data;
    def getNext(self):
        return self.next;
    def setData(self,newData):
        self.data=newData;
    def setNext(self,newNode):
        self.next=newNode;

temp=Node(93);
temp.setData(10);
print(temp.getData());
    
class UnorderedList:
    def __init__(self):
        self.head=None;
    def isEmpty(self):
        return self.head==None;
    def add(self,item):
        temp=Node(item);
        temp.setNext(self.head);
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
myList = UnorderedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)
print(myList.search(17))
myList.remove(54)
print(myList.search(54))