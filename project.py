from datetime import datetime
pwd=input("Enter the Password to access the application\n")
if(pwd!='password'):
    exit()
# Create a node
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
   


    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):

        

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp_node = temp_node.next
            if temp_node is None:
                break

        next = temp_node.next.next
        temp_node.next = None
        temp_node.next = next

    def printList(self):
        temp_node = self.head
        j=1
        while (temp_node):
            print(j,". Website Name:",temp_node.item[0],"  Username:",temp_node.item[1],"  Password:",temp_node.item[2],"\n")
            j=j+1
            temp_node = temp_node.next

    def search(self, x):
        self.i=0
        self.current=self.head
        while self.current != None:
            if self.current.item[0] == x:
                return True
            self.current = self.current.next
            self.i=self.i+1
        return False
    def deleteAllNodes(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
            print("All passwords are deleted successfully.")  

        
stack=[]
store=[]
llist = LinkedList()
while(1):
    choice=int(input("Enter 1 to add a password\nEnter 2 to search for a password\nEnter 3 to Delete Passwords\nEnter 4 to display all the passwords\nEnter 5 to update the password details\nEnter 6 to review security activities\nAny other key to exit\n"))
    if(choice==1):
        ele=(input("enter the website name "))
        store.append(ele)
        ele=(input("enter username "))
        store.append(ele)
        ele=(input("enter the Password"))
        store.append(ele)
        llist.insertAtEnd(store)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        stack.append(["password for ",store[0],"was added at",current_time])
        store=[]
    elif(choice==2):
        if llist.head==None:
            print("No Passwords added to search")
        else:
            ele1=input("Enter the website to search\n")
            if llist.search(ele1):
                print("Website name:",llist.current.item[0],"\nUsername:",llist.current.item[1],"\nPassword",llist.current.item[2])
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                stack.append(["password for ",ele1,"was searched at",current_time])
            else:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                stack.append(["password for ",ele1,"(not found)was searched at",current_time])
                print("Website not added in the password manger!! ")
    elif(choice==3):
        while(1):
            if llist.head==None:
                print("No Passwords added to delete")
                break
            choice1=int(input("Enter 1 to delete one password and 2 to delete all passwords and any other number to exit this option\n"))
            if(choice1==1):
                ele1=input("Enter the website to delete\n")
                if llist.search(ele1):
                    llist.deleteNode(llist.i)
                    print("Successfully deleted")
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    stack.append(["password for ",ele1,"was deleted at",current_time])
                    break
                else:
                    print("Website not added in the password manger!! ")
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    stack.append(["password for ",ele1,"(not found)was attempted to delete at",current_time])
                    break
            if(choice1==2):
                llist.deleteAllNodes()
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                stack.append(["All passwords ","were"," deleted at",current_time])
            else:
                break
    elif(choice==4):
        if llist.head==None:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            stack.append(["All ","passwords","were attempted to display(nothing was found) at",current_time])
            print("No Passwords added to display")
        else:
            llist.printList()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            stack.append(["All ","passwords","were displayed at",current_time])
    elif(choice==5):
        if llist.head==None:
            print("No Passwords added to update")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            stack.append(["A ","password","was attempted to update(but no passwords were in the apllication) at",current_time])
        else:
            k=input("enter the website name")
            if llist.search(k):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                stack.append(["Details for ",k,"was changed at",current_time])
                while(1):
                    d=int(input("enter 1 to update the website name, enter 2 to update the username and enter 3 to update the password and any other number to exit\n"))
                    if(d==1):
                        llist.current.item[0]=input("enter the website name to be changed\n")
                        break
                    elif(d==2):
                        llist.current.item[1]=input("enter the username to be changed\n")
                        break
                    elif(d==3):
                        llist.current.item[2]=input("enter the password to be changed\n")
                        break
                    else:
                        break
            else:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                stack.append(["Details for ",k,"was attempted to change(but not found) at",current_time])
                print("website not added in the application")
    elif(choice==6):
        j=1
        for x in range(len(stack)-1,-1,-1):
            y=stack[x]
            print(j,".",y[0],y[1],y[2],y[3])
            y=[]
            j=j+1
    else:
        exit()
