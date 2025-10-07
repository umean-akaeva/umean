class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        return f"{self.name} - {self.price} грн ({'в наявності' if self.available else 'нема'})"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.available:
            self.items.append(product)
            print(f"{product.name} додано в кошик.")
        else:
            print(f"{product.name} немає в наявності!")

    def remove_product(self, product_name):
        for p in self.items:
            if p.name == product_name:
                self.items.remove(p)
                print(f"{product_name} видалено з кошика.")
                return
        print(f"{product_name} не знайдено в кошику.")

    def total_price(self):
        total = sum(p.price for p in self.items)
        return total

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
        else:
            print("Товари у кошику:")
            for p in self.items:
                print(f"- {p.name}: {p.price} грн")
            print(f"Загальна вартість: {self.total_price()} грн")



p1 = Product("Ноутбук", 25000)
p2 = Product("Мишка", 500)
p3 = Product("Навушники", 1200, available=False)


cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.show_cart()
cart.remove_product("Мишка")
cart.show_cart()