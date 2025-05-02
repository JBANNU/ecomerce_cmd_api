from random import random
from rice_details import *
import sys



def order_bill(order,cu_name,total_price):

    with open("C:\\Users\\bjuloori\\OneDrive - DXC Production\\Desktop\\bill.txt","a+") as count_file:
        save_bill(order,cu_name,total_price) #saving the bill to txt
        sys.stdout=count_file
        save_bill(order,cu_name,total_price)
        
    return

            

def save_bill(order,cu_name,total_price):
    print("."*40)
    print("*"*13+"BILL"+"*"*14+"\n")
    print("CUSTOMER NAME:  "+cu_name,end="\n")
    print("Order items:    ")
    
    print(tabulate(order,headers=['bag_nme','quantity','price'],colalign=('left','left','center','right'),showindex=True,tablefmt='psql')) #for list we should give headers manuallu in tabulate
    print("\t\t\t total price: "+str(total_price))

    print("*"*40)
    print("contact details   0000-998-789")
    print("*"*40) 
    return

if __name__=='__main__':
    pass
   # order_bill()