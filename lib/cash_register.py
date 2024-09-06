#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for i in range(0, quantity):
            self.items.append(title)
        self.lastitem = title
        self.lastquantity = quantity
        self.lastprice = price

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.lastitem
            self.total -= self.lastquantity * self.lastprice * (self.discount / 100) if self.discount > 0 else self.lastquantity * self.lastprice
            print(f"The last item '{last_item}' has been removed from the register.")
        else:
            print("There are no items to void.")
