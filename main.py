
#costa = 0
#costb = 0
#costc = 0
cost = 0
unit = 0

fruit_type = ""

Fruit_options = ["apple", "grape", "orange"]

#apple = (f"1) {Fruit_options[0]}")
#grape = (f"2) {Fruit_options[1]}")
#orange =(f"3) {Fruit_options[2]}")

print("Welcome to the GC Fruit Market!")
name = input("What is your name?")
print(f"Welcome {name}")

print("The fruit options are:")

print(Fruit_options)

def my_function():
   global fruit_type
   fruit_type = input("Which fruit would you like to buy? ").lower()
   print(Fruit_options)

my_function()

fruit_price = {"apple": 2, "grape": 1, "orange": 3}

buy1 = f"1) You bought apples for ${fruit_price['apple']}"
buy2 = f"2) You bought grapes for ${fruit_price['grape']}"
buy3 = f"3) You bought oranges for ${fruit_price['orange']}"

if fruit_type == "apple":
   print(buy1)
   cost += fruit_price['apple']
   unit += 1

if fruit_type == "grape":
   print(buy2)
   cost += fruit_price['grape']
   unit += 1

if fruit_type == "orange":
   print(buy3)
   cost += fruit_price['orange']
   unit += 1

def another():
   global cost, unit
   fruit = input("Would you like to buy another piece of fruit? y/n").lower()
   if fruit in ['yes', 'y']:
       print(Fruit_options[0], Fruit_options[1], Fruit_options[2])
       my_function()
       another()
   else:
       print('Thank you for shopping. Goodbye!')

another()

print(f"Order for {name}")
print(f"{unit} apple(s) at $2 apiece")
print(f"{unit} grape(s) at $1 apiece")
print(f"{unit} orange(s) at $3 apiece")

tax = 0.25
subtotal = cost
total = cost + (cost + tax)

print(f"Subtotal: ${subtotal}")
print(f"5% Tax: ${subtotal + tax}")
print(f"Total: ${total}")
