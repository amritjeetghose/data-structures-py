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
        #to get the last node
        print(current_node.data)
    
    def printLinkedListAlt(self):
        current_node=self.head;
        while True:
            if(current_node.next == None):
                print(current_node.data)
                break;
            else:
                print(current_node.data)
                current_node=current_node.next;


    def lengthLinkedList(self):
        current_node=self.head;
        node_count=0;
        while True: 
            if(current_node.next ==None):
                node_count=node_count+1;
                break;
            else:
                node_count=node_count+1;
                current_node=current_node.next;
        print('linkedlist length=>', node_count)
    def insert_at_begining(self, data):
        new_node=Node(data);
        new_head=self.head;
        new_node.next=new_head;
        self.head=new_node;
    def print_updated_ll(self):
        current_node=self.head;
        while True: 
            if(current_node.next ==None):
                print('updated ll=>', current_node.data)
                break;
            else:
                print('updated ll=>', current_node.data)
                current_node=current_node.next;


llist = LinkedList()
#start inserting data in linkedlist
llist.insert_in_ll(1);
llist.insert_in_ll(2);
llist.insert_in_ll(3);
llist.insert_in_ll(4);
llist.insert_in_ll(5);
#print the linkedlist
llist.printLinkedList()
llist.printLinkedListAlt()
#print linkedlist length
llist.lengthLinkedList()
llist.insert_at_begining(0);

llist.print_updated_ll();