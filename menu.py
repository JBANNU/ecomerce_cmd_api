from art import text2art;
from decoraters import design_10;
from rice_details import *;

def menu():
    menu_1=text2art("MENU")
    print(menu_1)
    print("""
          1.details of menu of rice
          2.ordered details
          3.helpful contacts
          4.exit 
          """)
    selecte_menu = int(input("choose from menu"))
    return selecte_menu



      
      