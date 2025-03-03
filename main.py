from device import Smartphone, Laptop, Tablet  
from cart import Cart


devices = [
    Smartphone("iPhone 13", 999, 10, 24, 6.1, 20),
    Smartphone("Samsung Galaxy S22", 899, 15, 24, 6.5, 22),
    Laptop("MacBook Pro", 1999, 5, 36, 16, 3.2),
    Laptop("Dell XPS 15", 1799, 8, 24, 32, 3.5),
    Tablet("iPad Pro", 1299, 12, 24, "2732x2048", 600),
    Tablet("Samsung Galaxy Tab S8", 999, 9, 24, "2560x1600", 580),
]

cart = Cart()

def display_devices():
    """Displays all available devices."""
    print("\nAvailable Devices:")
    for index, device in enumerate(devices, start=1):
        print(f"{index}. {device}")

def add_to_cart():
    """Allows the user to add a device to the cart."""
    display_devices()
    try:
        choice = int(input("\nEnter the number of the device to add to cart: ")) - 1
        if 0 <= choice < len(devices):
            quantity = int(input(f"Enter quantity for {devices[choice].name}: "))
            cart.add_device(devices[choice], quantity)
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Please enter a valid number.")

def view_cart():
    """Displays items in the cart."""
    cart.print_items()

def checkout():
    """Processes the checkout."""
    cart.checkout()

def main():
    """Main menu loop."""
    while True:
        print("\nElectronic Device Shopping Cart")
        print("1. Show Devices")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_devices()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Exiting... Thank you for shopping!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

