#Importing the Python-MYSQL connector to connect our database
import mysql.connector as mysql

#Importing OS module to clear console
import os

# Function to clear console
''' This function will help us clear our console after a specific task
    so that our console may look friendly
    and easy to use. '''

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)


# Connecting to the existing IMS DATABASE
# These are the Queries we will use to connect to our existing Database.
# We use error handling to make efficient connection to our database.

try:
    db = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory ms"   # Here we can add the name of our exisitng database.
    )
    clearConsole()
    print("")
    print("\033[1m \t\tSuccessfully Connected To The DATABASE! \033[0m \n",)


except:
    clearConsole()
    print("\n")
    print(" \033[1m \t\tFailed To Connect To The Database\033[0m")
    print("\n")

command_handler = db.cursor()


# This is our main menu function. It will display all the available functions.

def menudisplay():
    
    print("===============================")
    print("  Inventory Management System  ")
    print("===============================")
    print("(1) Display all items")
    print("(2) Add New Item")
    print("(3) Remove Item")
    print("(4) Search Item")
    print("(5) Quit")
    
    CHOICE = eval(input("Enter choice: "))
    menuSelection(CHOICE)


# This function will take us to our desired task.
 
def menuSelection(CHOICE):
    if CHOICE==1:
        displayinventory()
    elif CHOICE==2:
         addinventory()
    elif CHOICE==3:
         removeinventory()
    elif CHOICE==4:
        searchinventory()
    elif CHOICE==5:
        exit() and clearConsole()
    else:
        print("No valid option was selected")


# This function is used to display all the available items in our database.
# We use MySQL queries to fetch data from table and display in our console.

def displayinventory():
    clearConsole()
    print("Displaying all items: ")
    print("=======================")

    command_handler = db.cursor()
    command_handler.execute("SELECT * FROM items")
    records = command_handler.fetchall()
    for record in records:
        print(record)
    
    CHOICE= input("Enter y to continue or n to exit: ")

    if CHOICE=="y":
        clearConsole()
        menudisplay()

    else: 
        clearConsole()


# This function will help us to add an item and its stock in the database.

def addinventory():
    clearConsole()
    print("Adding to the inventory")
    print("=======================")

    command_handler = db.cursor()

    query = "INSERT INTO items (name,stock) VALUES (%s, %s)"
    
    name = str(input("Enter name of the item: "))
    stock = str(input("Enter stock: "))
    query_vals = (name, stock)
    command_handler.execute(query, query_vals)
    
    db.commit()

    print(command_handler.rowcount, "records inserted!")
    
    CHOICE= input("Enter y to continue or n to exit: ")
    
    if CHOICE=="y":
        clearConsole()
        menudisplay()
    else: 
        clearConsole()

# This function is used to remove an existing item in our database.

def removeinventory():
    clearConsole()
    print("Removing an item from the inventory")
    print("===================================")

    command_handler = db.cursor()

    query = "DELETE FROM items WHERE name = (%s) "
    
    adr = str(input("Enter name of the item you want to remove: "))
    
    query_vals = (adr,)
    command_handler.execute(query, query_vals)
    
    db.commit()

    print(command_handler.rowcount, "records deleted")
   

    CHOICE= input("Enter y to continue or n to exit: ")
    
    if CHOICE=="y":
        clearConsole()
        menudisplay()
    else: 
        clearConsole()

# This module will help us to look for a specific item in our database along with its available stock.

def searchinventory():
    print("Searh in inventory")
    print("==================")

    command_handler = db.cursor()
    query = ("SELECT * FROM items WHERE name = %s")
    item_name = str(input("Enter name of the item: "))
    query_vals = (item_name,)
    command_handler.execute(query,query_vals)
    records = command_handler.fetchall()
    
    for record in records:
        print(record)
    

    CHOICE= input("Enter y to continue or n to exit: ")
    
    if CHOICE=="y":
        clearConsole()
        menudisplay()
    else: 
        clearConsole()

menudisplay()







