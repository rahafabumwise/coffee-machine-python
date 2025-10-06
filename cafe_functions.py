# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 19:49:17 2025

@author: Admin01
"""
import MENU

profit = 0
ingredients ={
        "water" : 200,
        "milk" : 150,
        "coffee" : 180,}
# a function to check if the user enter the right data
def validate_user_choice():
    valid_user_choices=["espresso","latte","cappuccino"]
    while True:
        choice= input("What would you like? (espresso/latte/cappuccino):").lower()
        if choice in valid_user_choices or choice in ["off","report"]:
            return choice
        print("❌ Invalid choice. Please choose espresso, latte, or cappuccino.")
        
# a funtion to check resources sufficient(is there enough product?)
def is_resource_sufficient(order_ingredients, drink):
    
    drink_needs = MENU.menu[drink]["ingredients"]
    if order_ingredients["water"] < drink_needs["water"]:
        return False,"Sorry there is not enough water."
    elif order_ingredients["coffee"] < drink_needs["coffee"]:
        return False,"Sorry there is not enough coffee."
    elif order_ingredients["milk"] < drink_needs["milk"] and drink != "espresso":
        return False,"Sorry there is not enough milk."
    else:
        return True,""

# a function to calculate the coins that the user enters        
def calculate_total_coins(total_coins):
    penny_value = total_coins["pennies"] * 0.01
    nickle_value = total_coins["nickles"] * 0.05
    dime_value = total_coins["dimes"] * 0.1
    quarter_value = total_coins["quarters"] * 0.25
    total = penny_value + nickle_value + dime_value + quarter_value
    return round(total,2)

# to check if the transaction is valid
def is_transaction_successful(money_insert, user_drink):
    reqeriment_money = MENU.menu[user_drink]["cost"]
    global profit
    if reqeriment_money > money_insert:
        return False,"Sorry that's not enough money. Money refunded."
    elif reqeriment_money == money_insert:
        profit += reqeriment_money
        return True,"Transaction completed successfully."
    else:
        refund = round(money_insert - reqeriment_money,2)
        profit += reqeriment_money
        return True,f"Transaction completed successfully.\nHere is ${refund} dollars in change."
    
 # makeing coffee(using the ingredients)      
def make_coffee(user_drink):
    global ingredients
    ingredients["water"] -= MENU.menu[user_drink]["ingredients"]["water"]
    ingredients["coffee"] -= MENU.menu[user_drink]["ingredients"]["coffee"]
    if user_drink != "espresso":
        ingredients["milk"] -= MENU.menu[user_drink]["ingredients"]["milk"]
    return f"here is your {user_drink}.🥰"

# a function to check coins validations(does the user enter the correct data?)
def get_coins_from_user():
    while True:
        try:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            return {
                "quarters" : quarters,
                "dimes"    : dimes,
                "nickles"  : nickles,
                "pennies"  : pennies,
                
                }
            
        except ValueError:
            print("Please enter a valid number.")