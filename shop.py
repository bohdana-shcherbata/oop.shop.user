class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop Name: {self.shop_name}")
        print(f"Store Type: {self.store_type}")

    def open_shop(self):
        print(f"The online shop '{self.shop_name}' is now open.")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, amount):
        self.number_of_units += amount


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products

    def get_discounts_products(self):
        print("Products with discounts:")
        for product in self.discount_products:
            print(f"- {product}")

store = Shop("MegaStore", "Electronics")
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()

store1 = Shop("FoodLand", "Groceries")
store2 = Shop("BookZone", "Books")
store3 = Shop("FashionPoint", "Clothes")

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print("Units:", store.number_of_units)
store.number_of_units = 50
print("Updated units:", store.number_of_units)

store.set_number_of_units(100)
print("Set units:", store.number_of_units)

store.increment_number_of_units(25)
print("Incremented units:", store.number_of_units)

store_discount = Discount("PromoStore", "Cosmetics", ["Lipstick", "Perfume", "Cream"])
store_discount.get_discounts_ptoducts()

all_store = Shop("TechWorld", "Gadgets")
all_store.open_shop()
