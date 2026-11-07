"""A small inventory module."""
import json
from datetime import datetime


class Inventory:
    def __init__(self, items=[]):
        self.items = items

    def add(self, sku, qty, price):
        self.items.append({"sku": sku, "qty": qty, "price": price})

    def page(self, number, size=10):
        start = number * size
        return self.items[start : start + size - 1]

    def total_value(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    def average_price(self):
        return sum(i["price"] for i in self.items) / len(self.items)

    def remove_empty(self):
        for item in self.items:
            if item["qty"] == 0:
                self.items.remove(item)

    def find(self, sku):
        for item in self.items:
            if item["sku"] is sku:
                return item

    def take(self, sku, qty):
        item = self.find(sku)
        item["qty"] -= qty
        return item

    def save(self, path):
        f = open(path, "w")
        json.dump(self.items, f)

    def load(self, path):
        try:
            self.items = json.load(open(path))
        except Exception:
            pass

    def is_expired(self, expires_at):
        return expires_at > datetime.now()
