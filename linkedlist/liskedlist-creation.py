#a node in the linkedlist
class Node:
    def __init__(self, data):
        #insert data in node
        self.data=data;
        #initialize next as none
        self.next=None;
class LinkedList:
    #initialize head as none
    def __init__(self):
        self.head=None;
    def insert_in_ll(self, data):
        #create a new node
        new_node=Node(data);
        #head is None meaning: no data in linkedlist
        if self.head is None:
            self.head=new_node;
        else:
        #linkedlist is not empty
            last=self.head;
            #traverse through linkedlist till last node is encountered
            while(last.next != None):
                last=last.next;
            # add new node as next of last node
            last.next=new_node;
    def printLinkedList(self):
        current_node=self.head;
        while(current_node.next != None):
            print(current_node.data)
            current_node=current_node.next;

llist = LinkedList()
#start inserting data in linkedlist
llist.insert_in_ll(1);
llist.insert_in_ll(2);
llist.insert_in_ll(3);
llist.insert_in_ll(4);
llist.insert_in_ll(5);
#sprint the linkedlist
llist.printLinkedList()