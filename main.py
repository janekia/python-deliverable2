class FruitMarket:
    def __init__(self):
        self.basket = {"Apple": 0, "Grape": 0, "Orange": 0}
        self.prices = {"Apple": 2, "Grape": 1, "Orange": 3}
        self.customer_name = ""

    def display_menu(self):
        print("Welcome to the GC Fruit Market!")
        self.customer_name = input("What is your name?\n> ")
        print(f"\nWelcome {self.customer_name}. Which Fruit would you like to buy?")

    def buy_fruit(self):
        while True:
            self.show_menu()
            choice = input("> ")

            if choice.isdigit() and 1 <= int(choice) <= 3:
                fruit_name = list(self.prices.keys())[int(choice) - 1]
                self.basket[fruit_name] += 1
                print(f"You bought 1 {fruit_name.lower()} at ${self.prices[fruit_name]}")

                if input("Would you like to buy another piece of fruit? y/n\n> ").lower() != 'y':
                    break
            else:
                print("Invalid choice. Please choose a valid option.")

    def show_menu(self):
        print("1. Apple $2\n2. Grape $1\n3. Orange $3")

    def calculate_total(self):
        sub_total = sum(self.basket[fruit] * self.prices[fruit] for fruit in self.basket)
        tax = 0.05 * sub_total
        total = sub_total + tax

        print(f"\nOrder for {self.customer_name}")
        for fruit, quantity in self.basket.items():
            print(f"{quantity} {fruit.lower()}(s) at ${self.prices[fruit]} apiece")

        print(f"Sub Total: ${sub_total:.2f}")
        print(f"5% Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")


def main():
    market = FruitMarket()
    market.display_menu()
    market.buy_fruit()
    market.calculate_total()


if __name__ == "__main__":
        main()
