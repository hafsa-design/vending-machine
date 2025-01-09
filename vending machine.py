class VendingMachine:
    def __init__(self):
        # Dictionary to store items and their prices
        self.items = {
            "Vanilla": 1.50,
            "Mango": 1.00,
            "Blueberry": 0.75,
            "Avocado": 1.25
        }

    def display_items(self):
        """Display the available items with prices."""
        print("Available items:")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")

    def process_transaction(self, item, money_inserted):
        """Process the transaction and check if the customer has enough money."""
        if item not in self.items:
            print(f"Sorry, we don't have {item} available.")
            return False

        price = self.items[item]

        if money_inserted >= price:
            change = money_inserted - price
            print(f"Dispensing {item}...")
            if change > 0:
                print(f"Your change is: ${change:.2f}")
            return True
        else:
            print(f"Insufficient funds. {item} costs ${price:.2f}, but you inserted ${money_inserted:.2f}.")
            return False

def main():
    machine = VendingMachine()

    while True:
        machine.display_items()

        # Ask the user to select an item
        item_choice = input("Please select an item (or type 'exit' to quit): ").capitalize()

        if item_choice.lower() == 'exit':
            print("Thank you for using the vending machine. Goodbye!")
            break

        # Ask how much money they want to insert
        try:
            money_inserted = float(input("Enter the amount of money you have: $"))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Process the transaction
        if not machine.process_transaction(item_choice, money_inserted):
            print("Transaction failed. Please try again.")

if __name__ == "__main__":
    main()
