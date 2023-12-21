

yes = "yes"
costa = 0
costb = 0
costc = 0
cost= 0
unit = 0
fruit_type = "you brought apples for $2"


print("Welcome to the GC Fruit Market!")
name = input("What is your name?")

Fruit_options = ["Apple ", "Grape ", "Orange"]
apple = (f"1) {Fruit_options[0]}")
grape = (f"2) {Fruit_options[1]}")
orange =(f"3) {Fruit_options[2]}")

print("The fruit options are:")

print(f"1) {Fruit_options[0]}")
print(f"2) {Fruit_options[1]}")
print(f"3) {Fruit_options[2]}")
fruit_type = input(f"Welcome {name}. Which Fruit would you like to buy?")

print(fruit_type)

if fruit_type == "1":
 costa += 2
 unit += 1
 print("you brought apples for $2")

if fruit_type == "2":
 costb += 1
 unit += 1
 print("you brought Grapes for $1")

if fruit_type == "3":
 costc += 3
 unit += 1
 print("you brought oranges for $3")

fruit = input("Would you like to buy another piece of fruit? y/n")
if fruit == 'yes' or 'Yes':
  print(apple,
        grape,
        orange)
else:
  breakpoint()


fruit_type = input("Which Fruit would you like to buy?")
print(fruit_type)

fruit = input("Would you like to buy another piece of fruit? y/n")
if fruit == 'yes' or 'Yes':
  print(apple,
        grape,
        orange)
else:
  breakpoint()

print(f"order for {name}")
print(f"{unit} apple(s) at ${costa} apiece")
print(f"{unit} grape(s) at ${costb} apiece")
print(f"{unit} oranges(s) at ${costc} apiece")
print(fruit_type)
price = (costa + costb + costc)
x = (price)

tax = .25

subtotal = print(f"subtotol ${price}")
Taxes = print(f"5% {tax}")
total: print(price + tax)
