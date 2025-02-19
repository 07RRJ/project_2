import os
import sys

os.system("cls")

lists = ""                    # variables

def show_list(lists):
    os.system("cls")
    print(list)

def add(lists, add):
    lists.append(add)
    return b

def remove(lists, ):
    lists.pop(x)

def change(x, y):
    list[x] = y

# def quit_(a):
#     sys.exit("you quit")

while True:                 # the main loop
    action = input("\"1\" to add\n\"2\" to remove\n\"3\" to change\n\"4\" or \"q\" to quit\n\n")
    if action.isdigit():
        action = float(action)
        print("action is an int")
    if action == 1:
        add(lists, x = input("add: "))
        print(lists)
    
    elif action == 2:
        remove(x = int(input(f"chose between 0 - {len(lists)} to remove it: ")))
    
    elif action == 3:
        change()

    elif action == 4:
        sys.exit("you quit")

    else: 
        print("you can only chose one of the 4 options above")

