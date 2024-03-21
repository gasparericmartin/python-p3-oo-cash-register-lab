#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.price_list= {}

  def add_item(self, title, price, quantity=1):
    for x in range(quantity):
      self.items.append(title)
    self.total += price * quantity
    self.price_list[title] = {'price': price, 'quantity': quantity}


  def apply_discount(self):
    self.total -= (self.total * self.discount * .01)
    if self.discount > 0:
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print('There is no discount to apply.')
  
  def new_register_items(self):
    return self.items

  def void_last_transaction(self):
    last_item = self.items[len(self.items) - 1]
    self.total -= self.price_list[last_item]['price'] * self.price_list[last_item]['quantity']
    del(self.items[len(self.items) - 1])
