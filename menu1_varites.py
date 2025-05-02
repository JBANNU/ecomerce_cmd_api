#varaites in menu
from decoraters import design_10;
from art import text2art;
from rice_details import *;
from menu import *;
from tabulate import tabulate;


def rice_menu():
        
        rice=read_data()
        print("""
        1.display all rice 
        2.display of particular type
        3.change price bag
        4.add a new type of rice
        5.add extra bags to inventory 
        6.correct the details of rice
        7.order the rice """)
        menu_select=int(input("select the option from above: "))

        match menu_select:
                case 1:
                    display_all_data(rice)
                case 2:
                    display_type(rice)
                case 3: 
                    change_price(rice)
                case 4:
                    add_new_stock(rice)
                case 5:
                    add_bags(rice)
                case 6:
                  correct_details(rice)
                case 7:
                  order_details(rice)
                case default:
                    print("enter the correct value from 1-7")
                    pass_th=True
        return 


