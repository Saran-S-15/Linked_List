class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printLL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.next
            
    def add_begin(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def add_end(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            new_node = Node(data)
            n.next = new_node
    
    def add_after(self,data,x):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("X is not present in the Linked List")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                
    def add_before(self,data,x):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        if x == self.head.data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                if x == n.next.data:
                    break
                n = n.next
            if n.next is None:
                print("X is not present in the Linked List")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Linked List is Empty, Can't Delete")
        else:
            self.head = self.head.next
            if self.head is None:
                print("Linked List is Empty, Can't Delete")
                
    def delete_end(self):
        if self.head is None:
            print("Linked List is Empty, Can't Delete")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    
    def delete_value(self,x):
        if self.head is None:
            print("Linked List is Empty, Can't Delete")
        else:
            if self.head.data == x:
                self.head = self.head.next
                return
            n = self.head
            while n.next is not None:
                if x == n.next.data:
                    break
                n = n.next
            if n.next is None:
                print("X is not present in the Linked List, Can't Delete")
            else:
                n.next = n.next.next
                
           
ll = LinkedList()
ll.add_begin(20)
ll.add_begin(10)
ll.add_end(30)
ll.add_after(500,20)
ll.add_before(1000,30)
ll.delete_begin()
ll.delete_end()
ll.delete_value(1000)
ll.printLL()