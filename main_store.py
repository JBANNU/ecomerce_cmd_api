from art import *;
from menu import menu;
from menu1_varites import rice_menu;
from decoraters import design_50,design_10,red,white;
from time import time;
from tabulate import tabulate
import webbrowser



if __name__=="__main__":
    ##banner
    a=text2art("shoppeeee")
    print(a)

    print("hi welcome back below is the menu: ")
    pass_th=True
    while pass_th:
        design_10()
        #--------------display menu---------
        selected_menu=menu()
    
    #--------------display sub-menu if ==1 ---------
        match selected_menu:
            case 1:
                rice_menu()
                pass_th=False
            case 2:
                 webbrowser.open("C:\\Users\\bjuloori\\OneDrive - DXC Production\\Desktop\\bill.txt")
            case 3:
                with open(".\\hepful.txt","r") as f:
                    details=f.read()
                    print(details)
                    f.close()
            case 4:
                pass_th=False
                exit(1)
            case default:
                print(red+"remianing under progress........bye"+white)
        exit_status=str(input("do you want to go back y/n: "))
        pass_th = True if exit_status == 'y' or 'Y' else False #teneray operator if in one line
       
    else:
        exit(1)
        #exiting(pass_th) if exit_status == False else pass_th  


