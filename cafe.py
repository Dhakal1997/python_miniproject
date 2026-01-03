# defining menu
menu = {'burger': 20 ,
        'sandwich':15,
        'sasta': 25,
        'salad': 30,
        'soup' : 20,
}

print("\n Welcome to Binita's Restaurant")
print("Burger: $20\nSandwich: $15\nPasta: $25\nSalad: $30\nSoup: $20")

order_total = 0

item_1 = input("Enter name of item you want to order = ").lower()
               
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to order")

else:
    print(f"your item {item_1} is  not on the menu yet")
 
another_order= input("Do you want to add more item{Yes/No}") 
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"your item {item_2} has been added to order") 
    else:
        print(f"your item {item_2} is not in menu yet") 
        
       
    
 
    
print(f"the total amount of item to pay is {order_total}")      
        

