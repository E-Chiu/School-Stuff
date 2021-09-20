class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        newHead = DLinkedListNode(item, self.__head, None)
        if self.__head != None:
            self.__head.setPrevious(newHead)
            self.__head = newHead
        else:
            self.__head = newHead
            self.__tail = newHead
        self.__size += 1

        
    def remove(self, item):
        current = self.__head
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        if found:
            if current.getPrevious() == None:
                self.__head = current.getNext()
                self.__head.setPrevious(None)
            if current.getNext() ==  None:
                self.__tail = current.getPrevious()
                self.__tail.setNext(None)
            else:
                prevNode = current.getPrevious()
                nextNode = current.getNext()
                prevNode.setNext(nextNode)
                nextNode.setPrevious(prevNode)
            self.__size -= 1
                
    def append(self, item):
        newTail = DLinkedListNode(item, None, self.__tail)
        if self.__tail != None:
            self.__tail.setNext(newTail)
            self.__tail = newTail
        else:
            self.__head = newTail
            self.__tail = newTail
        self.__size += 1
        
    def insert(self, pos, item):
        index = 0
        current = self.__head
        if pos ==  0:
            self.add(item)
        elif pos == self.__size:
            self.append(item)
        else:
            while index != pos:
                current = current.getNext()
                index += 1
            newNode = DLinkedListNode(item, current, current.getPrevious())
            current.setPrevious(newNode)
            temp = current.getPrevious()
            temp.setNext(newNode)
            self.__size += 1
        
    def pop1(self):
        current = self.__tail.getPrevious()
        temp = self.__tail
        if current != None:
            current.setNext(None)
        else:
            self.__head = current
        self.__tail = current
        self.__size -= 1
        return temp.getData()
        
    
    def pop(self, pos=None):
        if pos == None:
           return self.pop1()
        # Hint - incorporate pop1 when no pos argument is given
        else:
            index = 0
            current = self.__head
            while index != pos:
                current = current.getNext()
                index += 1
            if current.getPrevious() == None:
                self.__head = current.getNext()
                current.getNext().setPrevious(None)
            if current.getNext() ==  None:
                self.__tail = current.getPrevious()
                current.getPrevious().setNext(None)
            else:
                prevNode = current.getPrevious()
                nextNode = current.getNext()
                prevNode.setNext(nextNode)
                nextNode.setPrevious(prevNode)
            self.__size -= 1
            return current.getData()
        
    def searchLarger(self, item):
        current = self.__head
        pos = 0
        while current.getNext() != None:
            if current.getData() > item:
                return pos
            current = current.getNext()
            pos += 1
        return -1

        
    def getSize(self):
        return self.__size
    

    def getItem(self, pos):
        assert pos < self.__size, 'index out of range!'
        if pos < 0:
            current = self.__tail
            index = -1
            while pos != index:
                current = current.getPrevious()
                index -= 1
            return current.getData()
        elif pos >= 0:
            current = self.__head
            index = 0
            while pos != index:
                current = current.getNext()
                index += 1
            return current.getData()
        
    def __str__(self):
        if self.__head == None:
            return ''
        else:
            current = self.__head
            listString = str(current.getData())
        while current.getNext() != None:
            current = current.getNext()
            listString = listString + ' ' + str(current.getData())
        listString = listString
        return listString


def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   

    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()
