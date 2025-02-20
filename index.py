import os
import sys

os.system("cls")

lists = []                    # the list of doom
list_item = 0
item = ""

def add(new_item):              # add an item
    lists.append(new_item)

def remove(remove_item):              # remove a item
    lists.pop(remove_item - 1)          # the list doesnt start from 0 in the ui so -1 backend

def change(old_item, new_item):             # change an item with another one
    index = lists.index(old_item)
    lists[index] = new_item             

def just_list():                    # show the list content
    os.system("cls")
    print("=" * 100)
    print(" " * 45, "The list")
    for list_item, item in enumerate(lists, 1):          #correct way to show list items
        print(f"{list_item}) {item}")
    print("=" * 100)

def you_quit():             # quitting the application in a fancy pants way
    just_list()
    sys.exit("you quit")


def the_program():                # the program
    os.system("cls")
    print("=" * 100)
    print("\"1\" to add\n\"2\" to remove\n\"3\" to change\n\"4\" or \"q\" to quit\n")               # options
    for list_item, item in enumerate(lists, 1):          #and ctrl + c ctrl+ v to show the list in the menue, this is optional though in my opinion 
        print(f"{list_item}) {item}")
    print("=" * 100)
    action = input(": ")

    if action.isdigit():            # if you use any characters instead of numbers... should of used a try.... but idk
        action = float(action)

    if action == 1:                 # call the add function and show the list
        just_list()
        new_item = input("add: ")
        add(new_item)
        os.system("cls")

    elif action == 2:               #call the remove function and show what you can remove
        if len(lists) > 0:
            just_list()
            while True:
                try:                # yay... i used a try thingy
                    remove_item = int(input(f"remove 1 - {len(lists)}: "))
                    if remove_item > len(lists):
                        just_list()
                        print("items doenst exist")
                    else:
                        remove(remove_item)
                        os.system("cls")
                        break
                except:
                    just_list()
                    print(f"you can only choose between 1 - {len(lists)}")
        else:
            print("you dont have anything in your list yet")

    elif action == 3:                   # change an item with user input
        just_list()
        old_item = input("enter item to change: ")
        while True:
            if old_item in lists:
                new_item = input("enter the new item: ")
                change(old_item, new_item)
                os.system("cls")
                break
            else:
                print(f"404")

    elif action == 4 or "q":                # call the quit function, i could implement it every where in the code but im tierd....
        you_quit()

while True:             # the program function with a while loop so i have less indentations in the code in genneral 
    the_program()