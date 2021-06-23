class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrevious(self, newprevious):
        self.previous = newprevious


class Unorderedlist:
    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        print('None <-')
        print('Head ->', end='')
        while current != None:
            if current.getNext() == None:
                print(current.getData(), end='->')
            else:
                print(current.getData(), end='<->')
            current = current.getNext()
        print('None')

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        temp.setPrevious(None)
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
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                if current == None:
                    next = None
                else:
                    next = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            if current == None:
                previous.setNext(None)
            else:
                previous.setNext(current.getNext())
            if next != None:
                next.setPrevious(current.getPrevious)
        if current is None:
            print('Data not in list')


mylist = Unorderedlist()
mylist.add(31)
mylist.add(11)
mylist.add(15)
mylist.add(30)
mylist.show()