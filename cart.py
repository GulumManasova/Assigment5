class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            device.reduce_stock(amount)
            self.total_price += device.price * amount
            print(f"Added {amount} {device.name}(s) to the cart.")
        else:
            print(f"Not enough stock for {device.name}.")

    def remove_device(self, device, amount):
        for i, (cart_device, cart_amount) in enumerate(self.items):
            if cart_device == device:
                if amount >= cart_amount:
                    self.items.pop(i)
                    self.total_price -= cart_device.price * cart_amount
                else:
                    self.items[i] = (cart_device, cart_amount - amount)
                    self.total_price -= cart_device.price * amount
                print(f"Removed {amount} {device.name}(s) from the cart.")
                return
        print(f"{device.name} not found in cart.")

    def print_items(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\nItems in your cart:")
        for device, amount in self.items:
            print(f"{device.name} - {amount} pcs - ${device.price * amount}")
        print(f"Total Price: ${self.total_price}")

    def checkout(self):
        if not self.items:
            print("Cart is empty. Add items before checkout.")
            return
        print("\nCheckout successful! Your receipt:")
        self.print_items()
        self.items = []
        self.total_price = 0


    def checkout(self):
        for pair in self.items:
            self.device = pair[0]
            self.amount = pair[1]

            if (device_is.availiable(amount)):
                device.reduce_stock(amount)
                print(device,'Amount',amount)

