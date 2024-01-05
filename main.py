
cost = 0
fruit_counter = 0

fruit_type = ""

Fruit_options = ["apple $2", "grape $1", "orange $3"]

print("Welcome to the GC Fruit Market!")
name = input("What is your name?")
print(f"Welcome {name}")

print("The fruit options are:")
print(Fruit_options)

def my_function():
    global fruit_type, fruit_counter
    fruit_type = input("Which fruit would you like to buy? ").lower()
    fruit_counter = int(input("How many do you want to buy?"))
    print(Fruit_options)

my_function()

fruit_price = {"apple": 2, "grape": 1, "orange": 3}

buy1 = f"1) You bought apples for ${fruit_price['apple']}"
buy2 = f"2) You bought grapes for ${fruit_price['grape']}"
buy3 = f"3) You bought oranges for ${fruit_price['orange']}"

if fruit_type == "apple":
    print(buy1)
    cost += fruit_price['apple'] * fruit_counter

elif fruit_type == "grape":
    print(buy2)
    cost += fruit_price['grape'] * fruit_counter

elif fruit_type == "orange":
    print(buy3)
    cost += fruit_price['orange'] * fruit_counter

def another():
    global cost, fruit_counter
    fruit = input("Would you like to buy another piece of fruit? y/n").lower()
    if fruit in ['yes', 'y']:
        print(Fruit_options[0], Fruit_options[1], Fruit_options[2])
        my_function()
        another()
    else:
        print('Thank you for shopping. Goodbye!')

another()

print(f"Order for {name}")
print(f"{fruit_counter} apple(s) at $2 apiece")
print(f"{fruit_counter} grape(s) at $1 apiece")
print(f"{fruit_counter} orange(s) at $3 apiece")

tax = 0.25
subtotal = cost
total = subtotal + tax

print(tax)
print(f"5% Tax: ${subtotal}")
print(f"Total: ${total}")
