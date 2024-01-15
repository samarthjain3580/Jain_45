# Task3 Projects for beginner  
# Title: Shopping Items Inventory Management System 
# Description: 

# The Shopping Items Inventory Management System is designed to help businesses or stores manage their inventory of products efficiently.
# This system allows users to add, view, update, and remove items from the inventory.
# It also provides functionalities to display current stock details, including item name, price, quantity available, and category. 

# Features: 

# Add Items: Users can add new items to the inventory by providing details such as item name, price, quantity, and category. 
# View Inventory: Display the current list of items in the inventory along with their details (name, price, quantity, category). 
# Update Items: Allow users to modify details of existing items, such as updating price, quantity, or category. 
# Remove Items: Enable the removal of items from the inventory based on user selection. 
# Search Functionality: Implement a search feature to allow users to find specific items by name or category. 
# Inventory Reports: Generate reports summarizing inventory details, such as total number of items, total stock value, items low in stock, etc.

import pandas as pd

print("""\nShopping Items Inventory Management System:\n
Follow the Check-List given below- 
1.Add Items
2.Update Item
3.Remove Item
4.Search (Item/Category)
5.View Inventory
6.Stock Inventory Reports
7.Close Inventory""")

items=pd.DataFrame({'Items':[],'Price':[],'Quantity':[],'Catagory':[]})

items.loc[len(items)+1]=['pen',10,20,"a"]
items.loc[len(items)+1]=['pencil',5,2,'a']

while True:
    user=int(input("\nPress according to your Choice given above: "))
    # Add_Items
    if user==1 :
        item_name=input("\nWhich Item you want to Add: ")
        price=int(input("Price amount: ₹"))
        quantity=int(input("No. of Quantity: "))
        category=input("Which C1ategory: ")
        items.loc[len(items)+1]=[item_name,price,quantity,category]

    # Update_Items
    elif user==2:
        upd_item=input("\nWhich Item you want to Update: ")
        upd_item_index=list(items['Items']).index(upd_item)
        upd=int(input("Detail to Update (1.Price, 2.quantity, 3.category): "))
        if upd==1:
            upd_price=int(input("Updated Price: ₹"))
            items.iloc[upd_item_index,upd]=upd_price
        elif upd==2:
            upd_quantity=int(input("Updated Quantity: "))
            items.iloc[upd_item_index,upd]=upd_quantity
        elif upd==3:
            upd_category=input("Updated Category: ")
            items.iloc[upd_item_index,upd]=upd_category
        else:
            print("Invalid Number!")

    # Remove_Items
    elif user==3:
        rem_item=input("\nWhich Item you want to Remove: ")
        rem_item_index=list(items['Items']).index(rem_item)
        items.drop(rem_item_index+1,axis=0,inplace=True)

    # Search Functionality
    elif user==4:
        search_choice=int(input("\nSearch (1.Item, 2.Category): "))
        if search_choice==1:
            search_item=input("Which Item You Want to search: ")
            print('\n',items[items.Items==search_item])
        elif search_choice==2:
            search_category=input("Which Category You Want to search: ")
            print('\n',items[items.Catagory==search_category])
        else:
            print("Invalid Number1")

    # View_Inventory
    elif user==5:
        print('\n',items)

    # Inventory Reports
    elif user==6:
        print("\nTotal no. of Items in a Stock:",sum(list(items.Quantity)))
        print('\nTotal Stock Value: ₹',sum(items.Price*items.Quantity))
        
    elif user==7:
        break

    else:
        print("Error! Press Valid number from Checklist.")
