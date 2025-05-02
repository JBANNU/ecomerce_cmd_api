import json
from tabulate import tabulate
from decoraters import green,white,red,cyan
from ordered_list import *
import time
import os

def read_data():
     #making it avaliable to all
    with open("C:\\Users\\bjuloori\\OneDrive - DXC Production\\Documents\\Visual Studio 2022\\project\\rice_details.json",'r') as f:
        rice=json.loads(f.read())
        status_color(rice)
        #print(rice)
    f.close()
    return rice #returning the list of rice

#not for use, it is used by other funs, !!dont call directly
def write_data(r1):#taking the rice list
    with open("C:\\Users\\bjuloori\\OneDrive - DXC Production\\Documents\\Visual Studio 2022\\project\\rice_details.json",'w') as f:
        rice_data=json.dumps(r1,indent=2)
        f.write(rice_data)
        f.close()
    #print(rice)
    return

def change_price(r1):#taking list as r1
    display_all_data(r1)
    change_value=int(input("enter the number from above"))#selecting the name from above list to change price
    change_item=int(input("price you want to change: "))#taking the updated price value

    r1[change_value]['price']=change_item #changing price

    write_data(r1)
    display_all_data(r1)


    return

def order_details(r1):#passing the rice dict
    
    order_finish=True
    total_price=0
    order=[] #order list
    cu_name=str(input("enter the customer name: "))

    while order_finish:
    
        i1=0 #intialzing for index
        for i in range(0,len(r1)):
            print(i1,r1[i]['name'],end='\n') #displays the rice bage names
            i1+=1
        i1=0

        check_out_of_stock(r1)

        bag_order=int(input("enter bag name number: ")) #selecting the bag name
        bag_name=r1[bag_order]['name'] #storing the bag name
        bag_quantity=int(input("how many bags: ")) #entering number of bags
        bag_price=int(input("enter price given by customer: "))
        b=r1[bag_order]['count']-bag_quantity #checking if bags r present after client ask

        

        if r1[bag_order]['count'] >b and r1[bag_order]['count'] >0 and b>=0: #checking if have more than 0 bags
            
            order.append([bag_name,bag_quantity,bag_price]) #for billing purpose, appending the ordered
            total_price+=bag_quantity*bag_price
            

            a=r1[bag_order]['count']
            a=a-bag_quantity
            r1[bag_order]['count']=a #minus the taken bags and storing remaing

            check_out_of_stock(r1)

            write_data(r1) #rewriting to dictonary by calling write fun
            time.sleep(1)
            print(green+"updated iventory successfully!!!"+white)
            time.sleep(1)
            print("remaining quanity of "+bag_name+":  "+str(r1[bag_order]['count']))
            time.sleep(1)

            display_all_data(r1)

            time.sleep(1)
            print("given "+green+str(bag_quantity)+white+ " bags of "+cyan+bag_name+white)

        else:
            time.sleep(1)

            print(red+"out of stock!!!!!!! (or) insufficent"+white)
            time.sleep(1)

            display_all_data(r1)
        add_on=str(input("any others bags to add(y/n)"))
        order_finish = False if add_on == 'n' or 'N' else True

    order_bill(order,cu_name,total_price) #for billing

    return order_finish

def check_out_of_stock(r1): #checking inventory stock
    for i in range(0,len(r1)):
        if r1[i]['count']<=0:
            r1[i]['status']='out of stock'
            r1[i]['count']=0
        else:
            r1[i]['status']='avaliable'
    r1=status_color(r1)
    return r1

def display_all_data(r1):
    r1=check_out_of_stock(r1)
    r1=status_color(r1)
    os.system('cls')
    print(tabulate(r1,headers='keys',tablefmt='psql',showindex='always'))
    return


def status_color(r1):
    for i in range(0,len(r1)):
        if r1[i]['status']=='avaliable':
            r1[i]['status']=green+r1[i]['status']+white
        else:
            r1[i]['status']=red+r1[i]['status']+white
    return r1

def display_type(r1):#displaying only particular type
    print(""" 
        1.hmt_steam
        2.hmt_raw
        3.jsr_raw
        4.jsr_steam
        5.bpt_raw
        6.bpt_steam
        7.pelakadi
        8.broken """)
    select_type=int(input("select the type:"))
    rice_type: list[str]=[' ','hmt_steam','hmt_raw','jsr_raw','jsr_steam','bpt_raw','bpt_steam','pelakadi','broken'] #should add in the list
    new_rice_type: list=[['name','price','status','count']]
    for i in range(0,len(r1)):
        if r1[i]['type']==rice_type[select_type]:
            a=rice_type[select_type]#storing the rice name
            new_rice_type.append([r1[i]['name'],r1[i]['price'],r1[i]['status'],r1[i]['count']])
    os.system('cls')
    print("displaying detailsss of : "+green+a+white)
    print(tabulate(new_rice_type,headers='firstrow',tablefmt='psql',showindex='always'))

def add_bags(r1):
    display_all_data(r1)
    bag_no=int(input("select bag n0 from above: "))
    no_of_bags=int(input("how many bags want to add: "))
    r1[bag_no]['count']=r1[bag_no]['count']+no_of_bags
    write_data(r1)
    r1=check_out_of_stock(r1)
    write_data(r1)
    print(green+"added to the inventory"+white)
    return

def add_new_stock(r1):
    print("""
        Adding new baggg :)
          1.name
          2.type(hmt/bpt/jsrm)
          3.enter how many bags(count)
          4.price
           """)
    name=str(input('enter the name: '))
    type1=str(input('enter the type(hmt/bpt/jsrm): '))
    price=int(input('enter the price: '))
    bags=int(input('enter the no of bags: '))
    time.sleep(1)

    r1.append({
        'name':name,
        'type':type1,
        'price':price,
        'count':bags
    })

    r1=check_out_of_stock(r1)
    r1=status_color(r1)
    write_data(r1)
    display_all_data(r1)
    return

def correct_details(r1):
    #display_all_data(r1)
    for index,key in enumerate(r1[0]): #printing only kwy values, so user can select what he wants
        print(index,key)
    pass
    return 

def remove_rice(rice):
    pass

if __name__=="__main__":
    rice=read_data() #grabbing the list in rice
    #write_data(rice) == passing the rice list 
    #change_price(rice) 
    #order_details(rice)
    #display_all_data(rice)
    #display_type(rice)
    #add_new_stock(rice)
    #correct_details(rice)
    #add_bags(rice)
