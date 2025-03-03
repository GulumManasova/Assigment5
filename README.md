# Electronic Device Shopping Cart

This project is a simple **Electronic Device Shopping Cart System** that implements the Object-Oriented Programming (OOP) concept of **Inheritance** in Python. The system allows customers to browse electronic devices, add them to their shopping cart, and proceed to checkout.

## Table of Contents
1. Project Description
2. Classes and Methods
3. UML Class Diagram
4. How to Run the Project
5. Sample Input/Output
6. GitHub Repository Instructions

## 1. Project Description
The project simulates an electronic store where users can:
- View available devices (Smartphones, Laptops, Tablets)
- Add devices to their cart
- View the shopping cart
- Checkout and finalize the purchase
- Stock is automatically updated after purchase.

## 2. Classes and Methods

### Device (Base Class)
**Attributes:**
- `name`: Device name
- `price`: Device price
- `stock`: Available stock
- `warranty_period`: Warranty period in months

**Methods:**
- `__init__()`: Initializes common device attributes
- `display_info()`: Displays device details
- `apply_discount()`: Applies a discount on the price
- `is_available()`: Checks if the required quantity is available
- `reduce_stock()`: Reduces the stock after purchase

### Smartphone (Subclass)
**Attributes:**
- `screen_size`: Screen size in inches
- `battery_life`: Battery life in hours

**Methods:**
- `__str__()`: Displays smartphone details
- `make_call()`: Simulates making a call
- `install_app()`: Simulates app installation

### Laptop (Subclass)
**Attributes:**
- `ram_size`: RAM size in GB
- `processor_speed`: Processor speed in GHz

**Methods:**
- `__str__()`: Displays laptop details
- `run_program()`: Simulates running a program
- `use_keyboard()`: Simulates typing on the keyboard

### Tablet (Subclass)
**Attributes:**
- `screen_resolution`: Screen resolution
- `weight`: Weight in grams

**Methods:**
- `__str__()`: Displays tablet details
- `browse_internet()`: Simulates browsing the internet
- `use_touchscreen()`: Simulates using the touchscreen

### Cart Class
**Attributes:**
- `items`: List of items in the cart
- `total_price`: Total price of items in the cart

**Methods:**
- `add_device()`: Adds devices to the cart
- `remove_device()`: Removes devices from the cart
- `print_items()`: Prints all items in the cart
- `checkout()`: Finalizes purchase and reduces stock

## 3. UML Class Diagram
<img width="509" alt="Image" src="https://github.com/user-attachments/assets/093fd8f6-affc-48ad-8aab-f0ac92d8b1de" />

<img width="382" alt="Image" src="https://github.com/user-attachments/assets/3f2f3fc9-f042-4dca-a31d-e4fef3a56b83" />
