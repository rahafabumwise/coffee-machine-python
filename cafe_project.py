# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 15:42:14 2025

@author: Admin01
"""
import cafe_functions as cf

while True:

    user_order =  cf.validate_user_choice()
    
   
    if user_order == "off":
        print("Have a nice day.")
        break
        #turn off the machine
        
        
    elif user_order == "report":
        print(f"""
    ☕️ Current Resources:
    ------------------------
    Water   : {cf.ingredients["water"]}ml
    Milk    : {cf.ingredients["milk"]}ml
    Coffee  : {cf.ingredients["coffee"]}g
    Money   : ${cf.profit:.2f}
    ------------------------
    """)
        continue
    
    enough_resources, message1 = cf.is_resource_sufficient(cf.ingredients, user_order)
    print(message1)
    if enough_resources:
        coins = cf.get_coins_from_user()
        coins_total = cf.calculate_total_coins(coins)
        tx_ok, message2 = cf.is_transaction_successful(coins_total, user_order)
        print(message2)
        if tx_ok:
            message3 = cf.make_coffee(user_order)
            print(message3)
            
     
