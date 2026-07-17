#Final Project  
#Steve Young & Bradley Moore
#Version 1.0.2
#16 Jul 2026

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
            "Salad": 6.49,
            "Breadstick": 2.49
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
                ["Pizza", "Breadstick","Drink"]
            ),

            "Salad Combo": ComboMeal(
                "Salad Combo",
                8.99,
                ["Salad", "Breadstick", "Drink"]
            )
        }

        self.order = Order()

    def display_menu(self):
        # Update menu display using ASCII art
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
            "\nEnter item or combo: "
        ).strip().lower()

        # Case insensitive Addition
        menu_lookup = {name.lower(): name for name in self.menu}
        combo_lookup = {name.lower(): name for name in self.combos}
        
        if choice in menu_lookup:
            actual_name = menu_lookup[choice]
            item = MenuItem(actual_name, self.menu[actual_name])
            self.order.add_item(item)

        elif choice in combo_lookup:
            actual_name = combo_lookup[choice]
            self.order.add_item(self.combos[actual_name])

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
            return False

        # Update receipt display using ASCII art
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
        return True

    def run(self):
        while True:
            # Update options display using ASCII art
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
                if self.checkout():
                    break

            elif choice == "6":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid selection. Please try again.")


# Main Program
restaurant = Restaurant()
restaurant.run()
