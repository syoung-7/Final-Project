#Final Project  
#Steve Young & Bradley Moore

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ComboMeal(MenuItem):
    def __init__(self, name, price, included_items):
        super().__init__(name, price)
        self.included_items = included_items


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"\n{item.name} added to your order.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"\n{item.name} removed from your order.")
                return

        print("\nItem not found in order.")

    def display_order(self):
        if not self.items:
            print("\nYour order is empty.")
            return

        print("\n----- CURRENT ORDER -----")

        for item in self.items:
            print(f"{item.name:<20} ${item.price:.2f}")

        print("-" * 30)
        print(f"Subtotal: ${self.calculate_total():.2f}")

    def calculate_total(self):
        return sum(item.price for item in self.items)


class Restaurant:
    def __init__(self):

        # Dictionary for regular menu items
        self.menu = {
            "Burger": 8.99,
            "Pizza": 12.99,
            "Fries": 3.49,
            "Drink": 1.99,
            "Salad": 6.49
        }

        # Dictionary for combo meals
        self.combos = {
            "Burger Combo": ComboMeal(
                "Burger Combo",
                12.99,
                ["Burger", "Fries", "Drink"]
            ),

            "Pizza Combo": ComboMeal(
                "Pizza Combo",
                15.99,
                ["Pizza", "Drink"]
            ),

            "Salad Combo": ComboMeal(
                "Salad Combo",
                8.99,
                ["Salad", "Drink"]
            )
        }

        self.order = Order()

    def display_menu(self):
        print("\n========== MENU ==========")

        print("\nIndividual Items")

        for name, price in self.menu.items():
            print(f"{name:<15} ${price:.2f}")

        print("\nCombo Meals")

        for combo in self.combos.values():
            print(
                f"{combo.name:<15} "
                f"${combo.price:.2f} "
                f"({', '.join(combo.included_items)})"
            )

    def add_to_order(self):
        self.display_menu()

        choice = input(
            "\nEnter item or combo name exactly as shown: "
        )

        if choice in self.menu:
            item = MenuItem(choice, self.menu[choice])
            self.order.add_item(item)

        elif choice in self.combos:
            self.order.add_item(self.combos[choice])

        else:
            print("\nItem not found.")

    def remove_from_order(self):
        item_name = input(
            "\nEnter item or combo name to remove: "
        )

        self.order.remove_item(item_name)

    def checkout(self):
        if not self.order.items:
            print("\nNo items ordered.")
            return

        print("\n========== RECEIPT ==========")

        subtotal = self.order.calculate_total()
        tax_rate = 0.07
        tax = subtotal * tax_rate
        total = subtotal + tax

        for item in self.order.items:
            print(f"{item.name:<20} ${item.price:.2f}")

        print("-" * 30)
        print(f"Subtotal:      ${subtotal:.2f}")
        print(f"Tax (7%):      ${tax:.2f}")
        print(f"Grand Total:   ${total:.2f}")
        print("-" * 30)

        print("\nThank you for dining with us!")

    def run(self):
        while True:

            print("\n===== RESTAURANT ORDERING SYSTEM =====")
            print("1. View Menu")
            print("2. Add Item")
            print("3. Remove Item")
            print("4. View Order")
            print("5. Checkout")
            print("6. Exit")

            choice = input("\nChoose an option: ")

            if choice == "1":
                self.display_menu()

            elif choice == "2":
                self.add_to_order()

            elif choice == "3":
                self.remove_from_order()

            elif choice == "4":
                self.order.display_order()

            elif choice == "5":
                self.checkout()
                break

            elif choice == "6":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid selection. Try again.")


# Main Program
restaurant = Restaurant()
restaurant.run()
