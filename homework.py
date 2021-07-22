#Excercise 1
from IPython.display import clear_output

# Ask the user 5 bits of input: Do you want to : Show/Add/Delete/clear or Quit?
def shopcart():
    d = []
    while True:
        question = input("What would you like to do? Show/Add/Delete/Clear or Quit?")
        if question.lower() == "add":
            while True:
                shopitem = input("Type the item you would like to add. Type 'quit' once you are done.")
                if shopitem.lower() == "quit":
                    break
                elif shopitem.lower() not in d:
                    d.append(shopitem.lower())
                elif shopitem.lower() in d:
                    print("Item is already in shopping list.")
  
        elif question.lower() == "delete":
            while True:
                deleteitem = input("Type the item you would like to delete from list. Type 'quit' once you are done.")
                if deleteitem.lower() in d:
                    d.remove(deleteitem.lower())
                elif deleteitem.lower() == "quit":
                    break
                else: 
                    print("Item is not in shopping list. Please try again.")
            
        elif question.lower() == "clear":
            clearitem = input("Are you sure you want to clear the list? Yes/No.")
            if clearitem.lower() == "yes":
                d.clear()
            elif clearitem.lower() == "no":
                continue
            else:
                print("Invalid answer. Please try again.")
            
        elif question.lower() == "show":
            print(d)
        elif question.lower() == "quit":
            print(d)
            break
        else:
            print("Invalid answer. Please try again.")
        
shopcart()


#Exercise 2
from module3 import*
def calculate():
    while True: 
        question1 = input("Are you trying to find the square footage of a house or circle\'s circumference? Type \'c\'or \'s.\' Type 'quit' to quit.")
        if question1.lower() == "c": 
                cirquestion = input("What is the radius of the circle?")
                try:
                    print(circumference(int(cirquestion)))
                except ValueError:
                    print("Invalid number. Please try again.")
        elif question1.lower() == "s":
                length = input("What is the length of the house?")
                width = input("What is the width of the house?")
                try:
                    print(housesquare(int(length),int(width)))
                except ValueError:
                    print("Invalid number. Please try again.")
        elif question1.lower() == "quit":
            break
        else:
            print("Invalid answer. Please try again.")
                           
calculate()