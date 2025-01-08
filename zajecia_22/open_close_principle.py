# class DiscountCalculator:
#     def calculate_discount(self, customer_type, amount):
#         if customer_type == "Regular":
#             return amount * 0.9
#         elif customer_type == "Premium":
#             return amount * 0.8
#         elif customer_type == "VIP":
#             return amount * 0.5
#
#     def calculate_carrier_discount(self, customer_type, amount):
#         if customer_type == "Regular":
#             return amount * 0.9
#         elif customer_type == "Premium":
#             return amount * 0.8
#         elif customer_type == "VIP":
#             return amount * 0.5
#
# calculator = DiscountCalculator()
# print(f"Regular Customer: {calculator.calculate_discount('Regular', 100)}")
# print(f"VIP Customer: {calculator.calculate_discount('VIP', 100)}")

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):

    @abstractmethod
    def calculate(self):
        pass

class RegularDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.9

class PremiumDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.8

class VIPDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.5


regular_discount = RegularDiscount()