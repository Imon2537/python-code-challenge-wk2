# coffee class is initiated and name instance is created
class Coffee:
    def __init__(self, name):
        self.name = name
        print(f"Created coffee: {self.name}")
    #a getter method that allows this method to be accessed as an attribute and is called when coffee.name is called 
    @property
    def name(self):
        return self._name
    # this setter method sets a new value in to the new name
    @name.setter
    def name(self, new_name):
        # it checks if the private attribute _name exist wich prevents modifying the name after the object is created
        if not hasattr(self, "_name"):
            # checks if the new_name is a string and its atleast 3 characters long
            if type(new_name) == str and 3 <= len(new_name):
                self._name = new_name
            else:
                raise ValueError("Name must be 3 or more characters")
    # it returns all orders associated with this coffee instance
    def orders(self):
        # it filters the global list order.all to find the order where order.coffee matches the current coffee instance inside the global order list hence order.coffee
        orders_for_coffee = [order for order in Order.all if order.coffee == self]
        print(f"Orders for {self.name}: {orders_for_coffee}")
        return orders_for_coffee
    # this method retrieves all unique customers who ordered this coffee 
    def customers(self):
        # creates a set af customer who placed orders for this coffee based on the orders retrieved in orders() method
        customer_list = list({order.customer for order in self.orders()})
        print(f"Customers who ordered {self.name}: {customer_list}")
        return customer_list
    # this method returns the total number of orders for this coffee
    def num_orders(self):
        # calculates the number of orders by getting the length of the list returned by the orders method
        num = len(self.orders())
        print(f"Number of orders for {self.name}: {num}")
        return num
    # this method calculates the average price for all orders
    def average_price(self):
        # this if statement checks if there are no orders it prints the average price of 0
        if self.num_orders() == 0:
            print(f"No orders for {self.name}, so average price is 0.")
            return 0
        # calculates the total sum of all orders by iterating over all the orders and summing up the prices
        sum_prices = sum([order.price for order in self.orders()], 0)
        # it divides the total sum of prices by the numbers of orders to get the avg price
        avg_price = sum_prices / self.num_orders()
        print(f"Average price for {self.name}: {avg_price}")
        return avg_price

#  a class called customer is created and a name instance is created
class Customer:
    def __init__(self, name):
        self.name = name
        print(f"Created customer: {self.name}")
    #a getter method that allows this method to be accessed as an attribute and is called when customer.name is called
    @property
    def name(self):
        return self._name
    # it checks if the customers name is valid and if the name is a string between 1- 15 characters 
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and 1 <= len(new_name) <= 15:
            self._name = new_name
    # retreives all orders made by this customer
    def orders(self):
        # filters the global list where order.customer is this customer instance created and returns a list of orders
        customer_orders = [order for order in Order.all if order.customer == self]
        print(f"{self.name}'s orders: {customer_orders}")
        return customer_orders
    # returns all coffee ordered by this customer 
    def coffees(self):
        # it returns a set of coffee based on the orders the orders the customer has made and prints the list
        customer_coffees = list({order.coffee for order in self.orders()})
        print(f"{self.name}'s coffees: {customer_coffees}")
        return customer_coffees
    # creates a new order instance using the customer ,coffee, price  
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        print(f"{self.name} created an order for {coffee.name} at ${price}")
        return new_order

# a class called order is created
class Order:
    # keeps track of all order instances
    all = []
    # attributes customer, coffee, price are created and the newly created order is added in the order.all list 
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        print(f"New order created: {self.customer.name} ordered {self.coffee.name} for ${self.price}")
    # this getter method returns the price 
    @property
    def price(self):
        return self._price
    # this setter method sets a new value to to the new price 
    @price.setter
    def price(self, new_price):
        # checks if the private attribute _price exist to prevent modifying the price after the object is created 
        if not hasattr(self, "_price"):
            # checks if the new price is a float  and its between 1.0 and 10.0 and if valid it sets the price
            if isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
                self._price = new_price
            else:
                raise ValueError("Price must be a float between 1.0 and 10.0")
    # this getter method returns the customer
    @property
    def customer(self):
        return self._customer
    # this setter method ensures that the new customer is a valid customer instance
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
     # this getter method returns the coffee
    @property
    def coffee(self):
        return self._coffee
    # this setter method ensures that the new coffee is a valid customer instance
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee


# Testing the code with outputs
if __name__ == "__main__":
    # sets the name attribute using the setter method in coffee class
    espresso = Coffee("Espresso")
    latte = Coffee("cappucino")

    #sets the name attribute using the setter method in customer class 
    john = Customer("John")
    jane = Customer("Jane")

    # it triggers the create_order method in the customer class
    john_order = john.create_order(espresso, 5.0)
    jane_order = jane.create_order(latte, 4.5)

    # Testing Coffee methods
    espresso.orders()
    espresso.customers()
    espresso.num_orders()
    espresso.average_price()

    latte.orders()
    latte.customers()
    latte.num_orders()
    latte.average_price()

    # Testing Customer methods
    john.orders()
    john.coffees()
    jane.orders()
    jane.coffees()
    
    