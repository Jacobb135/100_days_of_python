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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True
resources["money"] = 0
def pull_resources(resource):
    if resource == "espresso":
        MENU["espresso"]["ingredients"]["milk"] = 0
    water = MENU[resource]["ingredients"]["water"]
    milk = MENU[resource]["ingredients"]["milk"]
    coffee = MENU[resource]["ingredients"]["coffee"]
    if water > resources["water"]:
        print("Sorry there is not enough water")
        machine_on = False
    elif milk > resources["milk"]:
        print("Sorry there is not enough milk")
        machine_on = False
    elif coffee > resources["coffee"]:
        print("Sorry there is not enough coffee")
        machine_on = False

def user_entry(user_prompt):
    if user_prompt == "espresso":
        pull_resources("espresso")
        process_coins("espresso")
    elif user_prompt == "latte":
        pull_resources("latte")
        process_coins("latte")
    elif user_prompt == "cappuccino":
        pull_resources("cappuccino")
        process_coins("latte")
    elif user_prompt == "off":
        machine_on = False
    elif user_prompt == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        resources["money"] = 0
        money = resources["money"]
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

def process_coins(prompt):
    print("PLease insert coins")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))
    total_amount = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    print(total_amount)
    print(MENU[prompt]["cost"])
    if total_amount >= MENU[prompt]["cost"]:
        refund_amount = round(total_amount - MENU[prompt]["cost"], 2)
        print(f"Money refunded: {refund_amount}")
        resources["milk"] -= MENU[prompt]["ingredients"]["milk"]
        resources["coffee"] -= MENU[prompt]["ingredients"]["coffee"]
        resources["water"] -= MENU[prompt]["ingredients"]["water"]
        resources["money"] += MENU[prompt]["cost"]
        print(resources)
    elif total_amount < MENU[prompt]["cost"]:
        print(f"Sorry that's not enough money. Money refunded ${total_amount}")

while machine_on:
    prompt = input("What would you like? (espresso/latte/cappuccino) ").lower()
    user_entry(prompt)

