"""
Group members : 
Amira Shalgimbayeva line 91 to 164
Tanya Navani line 40 to 88, 144 to 164


This code deals with the shopping cart where you can add and remove items or products that are mentioned in the csv file along with their 
price, quantity, inventory. This code contains classes Article and Cart along with the functions main and inventory which helps uss to
calculate the price and checkout.
"""

import csv

class Article: 
    """
    A class Article that has the following attributes name, price and quantity. 
    The Article class have the following method/constructor def __init__()
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self): ## Returns the name of the item
        return self.name

    def getPrice(self): ## Returns the price of the item
        return self.price

    def getQuantity(self): ## Returns the quantity of the item
        return self.quantity

    def setQuantity(self, quantity): ## Takes a quantity as parameter and reset the quantity of the article to be equal to quantity.
        self.quantity = quantity

    def __str__(self): ## Creates a string representation of an Article object
        return f"Article: {self.name}, Quantity: {self.quantity}, Price: {self.price}"


class Cart:
    """
    Shows the shopping cart with the items.
    """
    def __init__(self): ## Is the constructr of the class
        self.list_of_purchased = []

    def addProduct(self, name, quantity, inventory): ## Adds the item to the cart
        if name in inventory: 
            available_quantity = min(quantity, inventory[name].getQuantity()) ## checks if the item is already in the cart
            for article in self.list_of_purchased:
                """
                lint 52 if item is present, line 53 adds the quantity, 54-55 adds item and the quantity
                """
                if article.getName() == name: 
                    article.setQuantity(article.getQuantity() + available_quantity)
                    inventory[name].setQuantity(inventory[name].getQuantity() - available_quantity)
                    return
            self.list_of_purchased.append(Article(name, inventory[name].getPrice(), available_quantity))
            inventory[name].setQuantity(inventory[name].getQuantity() - available_quantity)

    def removeProduct(self, name, quantity, inventory): ## Removes the item from the cart
        for article in self.list_of_purchased:
            """
            line 65-66 if the quantity is greater or equal than specified quantity, then whole article will be removed
            """
            if article.getName() == name:
                if quantity >= article.getQuantity():
                    inventory[name].setQuantity(inventory[name].getQuantity() + article.getQuantity())
                    self.list_of_purchased.remove(article)
                else: ## Reduction of the quantity
                    article.setQuantity(article.getQuantity() - quantity)
                    inventory[name].setQuantity(inventory[name].getQuantity() + quantity)
                return

    def displayCart(self): 
        """
        Displays the items in the cart
        """
        if self.list_of_purchased == []:
            print("Sorry the shopping cart is empty") ## If no items are present, this is printed
        for article in self.list_of_purchased:
            print(article) 

    def checkout(self): ## Gives the total amount to be paid
        total_price = 0
        for article in self.list_of_purchased:
            total_price += article.getPrice() * article.getQuantity() ## Calculates the total amount by multiplying amount and quantity
        return total_price


def menu():
    ## Displaying of the menu
    print("1. List all items, inventory and price")
    print("2. List cart shopping items")
    print("3. Add an item to the shopping cart")
    print("4. Remove an item from the shopping cart")
    print("5. Checkout")
    print("6. Exit")


def displayInventory(inventory): ## Displayed if choice 1 is selected
    inventory_dict = {name: (article.getQuantity(), article.getPrice())
                      for name, article in inventory.items()} 
    print(inventory_dict)

"""
Shows the content of csv file
"""
def readInventoryFromCSV(filename): 
    INVENTORY = {}
    with open(filename, 'r') as file: ## Reads the csv file
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            price = float(row['price'])
            quantity = int(row['inventory'])
            INVENTORY[name] = Article(name, price, quantity) ## Displayed in inventory_dict
    return INVENTORY


def main():
    file = "products.csv"
    INVENTORY = readInventoryFromCSV(file)
    shoppingCart = Cart()
    while True:
        menu()
        """
        Calls certain functions with a certain choices. 
        Choice 1 calls displayInventory() function
        Choice 2 displays the list of items in the shopping cart
        Choice 3 adds name and quantity of the item to the shopping cart
        choice 4 removes an item and the quantity from the cart
        Choice 5 prints the total orice of the items
        """
        choice = input("Enter your choice: ")
        if choice == "1":
            displayInventory(INVENTORY) 
        elif choice == "2":
            shoppingCart.displayCart()
        elif choice == "3":
            name = input("Add an item from our catalogue to the shopping cart: ")
            quantity = int(input("Add the quantity: "))
            shoppingCart.addProduct(name, quantity, INVENTORY)
        elif choice == "4":
            name = input("Remove an item from the shopping cart: ")
            quantity = int(input("Remove the quantity of item from the shopping cart: "))
            shoppingCart.removeProduct(name, quantity, INVENTORY)
        elif choice == "5":
            total_price = shoppingCart.checkout()
            print(f"Total Price: {total_price:.2f}")
            break
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

        continueShopping = input("Do you want to continue (y/n)? ")
        if continueShopping.lower() != "y":
            break


if __name__ == "__main__":
    main()