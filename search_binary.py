 
class node:
    def __init__(self, data):
        self.data= data
        self.next = None

class Linkedlist:
    def __init__(self):

        self.head = None
        

    def push(self, new_data):

        new_node =  node(new_data)

        new_node.next = self.head
        self.head = new_node


    def search(self, key):

        curr = self.head
        
        while(curr):
            if(curr.data==key):
                return True
            curr = curr.next

        #if data not found
        return False
