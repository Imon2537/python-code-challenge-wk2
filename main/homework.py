class Coffee:
    def __init__(self, name):
        self.name = name
        print(f"Created coffee: {self.name}")
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            if type(new_name) == str and 3 <= len(new_name):
                self._name = new_name
            else:
                raise ValueError("Name must be 3 or more characters")

    def orders(self):
        orders_for_coffee = [order for order in Order.all if order.coffee == self]
        print(f"Orders for {self.name}: {orders_for_coffee}")
        return orders_for_coffee
    
    def customers(self):
        customer_list = list({order.customer for order in self.orders()})
        print(f"Customers who ordered {self.name}: {customer_list}")
        return customer_list
    
    def num_orders(self):
        num = len(self.orders())
        print(f"Number of orders for {self.name}: {num}")
        return num
    
    def average_price(self):
        if self.num_orders() == 0:
            print(f"No orders for {self.name}, so average price is 0.")
            return 0
        sum_prices = sum([order.price for order in self.orders()], 0)
        avg_price = sum_prices / self.num_orders()
        print(f"Average price for {self.name}: {avg_price}")
        return avg_price


class Customer:
    def __init__(self, name):
        self.name = name
        print(f"Created customer: {self.name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) == str and 1 <= len(new_name) <= 15:
            self._name = new_name
    
    def orders(self):
        customer_orders = [order for order in Order.all if order.customer == self]
        print(f"{self.name}'s orders: {customer_orders}")
        return customer_orders
    
    def coffees(self):
        customer_coffees = list({order.coffee for order in self.orders()})
        print(f"{self.name}'s coffees: {customer_coffees}")
        return customer_coffees
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        print(f"{self.name} created an order for {coffee.name} at ${price}")
        return new_order


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        print(f"New order created: {self.customer.name} ordered {self.coffee.name} for ${self.price}")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if not hasattr(self, "_price"):
            if isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
                self._price = new_price
            else:
                raise ValueError("Price must be a float between 1.0 and 10.0")

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee


# Testing the code with outputs
if __name__ == "__main__":
    # Create Coffee instances
    espresso = Coffee("Espresso")
    latte = Coffee("cappucino")

    # Create Customer instances
    john = Customer("John")
    jane = Customer("Jane")

    # John orders Espresso
    john_order = john.create_order(espresso, 5.0)
    
    # Jane orders Latte
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
    jane.coffees()
    print(espresso.name)
    print(latte.name)