class Stock:
    counter = 0
    stock_set = set()

    def __init__(self, stock_code, desc, price, available):
        self.stock_code = stock_code
        self.desc = desc
        self.price = price
        self.available = available
        Stock.counter += 1
        Stock.stock_set.add(self.desc)

    def sell_price(self):
        sp = round(self.price, 2)
        print('cost = $', sp)

    def label(self):
        print(f"{self.desc} costs you {self.price}")

    def sale(self, discount):
        new_sp = round(self.price * (1 - discount), 2)
        print('the discounted price of {} is $ {}'.format((self.stock_code, self.desc), new_sp))
        return new_sp


class Chocolate(Stock):

    category = 'chocolate'

    def __init__(self, stock_code, desc, price, available):
        super().__init__(stock_code, desc, price, available)

    def __repr__(self):
        print("You have chosen = {self.label}")


class Chips(Stock):
    category = 'chips'

    def __init__(self, stock_code, desc, price, packet_size, flavour, available):
        Stock.__init__(self, stock_code, desc, price, available)
        self.packet_size = packet_size
        self.flavour = flavour

    def __repr__(self):
        print("You have chosen = {self.label}")

    def one_for_one(self):
        # buy one get one offer
        sp = round(self.price, 2)
        print('Buy two packets of {} and get one free. You pay {}'.format(self.packet_size, sp))


class Canned(Stock):
    category = 'cans'

    def __init__(self, stock_code, desc, price, volume, available):
        Stock.__init__(self, stock_code, desc, price, available)
        self.volume = volume

    def label(self):
        print(f'{self.desc}')
        self.sell_price()

    def apply_discount(self, discount):
        new_sp = self.sale(discount)
        print('Price reduced ! you save = $ ', self.price - new_sp)


def choose_product(product):
    product_name = product.stock_code
    product_count = product.available
    print("$"*100)
    print(f"You have chosen {product_name} {product.desc}")
    if product_count != 0:
        print(f"feed in atleast {product.price} or more: ")
        money = float(input())
        if money > product.price:
            balance = money - product.price
            print(f"Here is the balance : {balance}")
            product.available -= 1
        elif money == product.price:
            print("Perfect Change - Thank you")
            product.available -= 1
        else:
            print("Feed in more cash/coin")
    print("$"*100)
    print("Thank you for choosing this vending machine")
    print("$"*100)


class VendingMachine:
    def __init__(self):
        self.money = 0
        self.products = {}

    def stock_details(self, product):
        d2 = {product.desc: {}}
        d2[product.desc]['price'] = product.price
        d2[product.desc]['quantity'] = product.available
        if product.stock_code == 'Can':
            d2[product.desc]['volume'] = product.volume
            self.products.setdefault(product.stock_code, {}).update(d2)
        elif product.stock_code == 'Chips':
            d2[product.desc]['flavour'] = product.flavour
            d2[product.desc]['packet_size'] = product.packet_size
            self.products.setdefault(product.stock_code, {}).update(d2)
        else:
            self.products.setdefault(product.stock_code, {}).update(d2)

    def display_vending_machine(self):
        for i, v in self.products.items():
            print(i, v)


print('****************************************************************')

final_product_set = ()
ca_1 = Canned('Can', 'Coke', 5.00, 500, 5)
ca_2 = Canned('Can', 'Pepsi', 4.00, 250, 4)
ch_1 = Chips('Chips', 'Potato', 10.00, 100, 'salt', 2)
ch_2 = Chips('Chips', 'Tapioco', 10.00, 100, 'chilly', 3)
chl_1 = Chocolate('Chocolate', 'Kitkat', 1.00, 15)
chl_2 = Chocolate('Chocolate', 'Hersheys', 2.00, 20)
print("Total number of products available: ",Stock.counter)
print("products = ", Stock.stock_set)
vm = VendingMachine()
vm.stock_details(ca_1)
vm.stock_details(ca_2)
vm.stock_details(ch_1)
vm.stock_details(ch_2)
vm.stock_details(chl_1)
vm.stock_details(chl_2)
vm.display_vending_machine()
choose_product(ch_1)
vm.stock_details(ch_1)
vm.display_vending_machine()

