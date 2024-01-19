#Cristian 
#01/12/24
#To-Do List

grocerylist= ["milk","chips","eggs","bananas"]



#Functions
def addtask():
    answ=input("What item would you like to add?:")
    grocerylist.insert(5,answ)
    menu()
    

def completedtask():
    print(grocerylist)
    ans = input("Please enter an item to check off: ")
    i = grocerylist.index(ans)
    grocerylist[i] = ans + " " + "X"
    menu()
    

def removetask():
    print ("Which item would you like to remove?: ")
    print (grocerylist)
    item=input("Item: ")
    if item == "milk":
        grocerylist.pop(0)
    elif item == "chips":
        grocerylist.pop(1)
    elif item == "eggs":
        grocerylist.pop(2)
    elif item == "bananas":
        grocerylist.pop(3)
    menu()




    
def menu():
    print ("Please choose an option: (Type in number between 1-5)")
    print ("1. Add a task to the To-Do List \n2. View the current To-Do List \n3. # Of Items \n4. Mark a task as completed \n5. Sort items alphabetically \n6. Remove a task from the grocery list \n7. Clear list \n8. Exit The Program")
    option=int(input("Option:"))
    if option == 1:
        addtask()
    if option == 2:
        print (grocerylist)
        menu()
    if option == 3:
       print(str(len(grocerylist)) + " " + "items")
       menu()
    if option == 4:
        completedtask()
    if option == 5:
        grocerylist.sort()
        menu()
    if option == 6:
        removetask()
    if option == 7:
        grocerylist.clear()
        menu()
    if option == 8:
        quit()
    





#Main
menu()