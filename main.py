#Dictionary of coffee types
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
#Resources Dictionary
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user_input = input("What would you like? (espresso/latte/cappuccino):")


total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]


if user_input == "espresso":
    used_water = total_water - MENU[user_input]["ingredients"]["water"]
    used_coffee = total_coffee - MENU[user_input]["ingredients"]["coffee"]
    used_milk = total_milk
elif user_input == "latte":
    used_water = total_water - MENU[user_input]["ingredients"]["water"]
    used_coffee = total_coffee - MENU[user_input]["ingredients"]["coffee"]
    used_milk = total_milk - MENU[user_input]["ingredients"]["milk"]
elif user_input == "cappuccino":
    used_water = total_water - MENU[user_input]["ingredients"]["water"]
    used_coffee = total_coffee - MENU[user_input]["ingredients"]["coffee"]
    used_milk = total_milk - MENU[user_input]["ingredients"]["milk"]
else:
    used_water = total_water
    used_coffee = total_coffee
    used_milk = total_milk
print(f"Water: {used_water}ml\nMilk: {used_milk}ml\nCoffee: {used_coffee}g")


# TODO: Print report for all the coffee machine resources

can_make_espresso = False
can_make_cappuccino = False
can_make_latte = False

if user_input == "espresso" and (used_water > MENU[user_input]["ingredients"]["water"] or used_coffee > MENU[user_input]["ingredients"]["coffee"]):
    can_make_espresso = True
elif user_input == "latte" and (used_water > MENU[user_input]["ingredients"]["water"] or used_milk > MENU[user_input]["ingredients"]["milk"] or used_coffee > MENU[user_input]["ingredients"]["coffee"]):
    can_make_latte = True
elif user_input == "cappuccino" and (used_water > MENU[user_input]["ingredients"]["water"] or used_milk > MENU[user_input]["ingredients"]["milk"] or used_coffee > MENU[user_input]["ingredients"]["coffee"]):
    can_make_cappuccino = True
else:
    can_make_espresso = False
    can_make_latte = False
    can_make_cappuccino = False
