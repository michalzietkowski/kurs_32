# class Order:
#     def __init__(self, customer, items):
#         self.customer = customer
#         self.items = items
#
#     def calculate_total(self):
#         return sum([item.get("price") * item.get("quantity") for item in self.items])
#
#     def generate_invoice(self):
#         return (f"Invoice for {self.customer}\n" +
#                 "\n".join([f"{item.get('name')} - {item.get('price')} x {item.get('quantity')}" for item in self.items]))
#
#     def process_payment(self):
#         total = self.calculate_total()
#         print(f"Payment processed for {total}")
#
#
# order = Order("Michal", [{"name": "Book", "price": 10, "quantity": 2},
#                         {"name": "Pen", "price": 1, "quantity": 5}])
#
#
# print(order.calculate_total())
# print(order.generate_invoice())
# order.process_payment()


class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items

    def calculate_total(self):
        return sum([item.get("price") * item.get("quantity") for item in self.items])


class InvoiceGenerator:
    def generate(self, order):
        total = order.calculate_total()
        return (f"Invoice for {order.customer}\n" +
                "\n".join([f"{item.get('name')} - {item.get('price')} x {item.get('quantity')}" for item in order.items])
                + f"\nTotal: {total}")

class PaymentProcessor:
    def process(self, order):
        total = order.calculate_total()
        print(f"Payment processed for {total}")

order = Order("Michal", [{"name": "Book", "price": 10, "quantity": 2},
                            {"name": "Pen", "price": 1, "quantity": 5}])

order_2 = Order("Adam", [{"name": "Book", "price": 10, "quantity": 2},
                            {"name": "Pen", "price": 2, "quantity": 5}])

invoice_generator = InvoiceGenerator()
invoice_generator.generate(order)

invoice_generator.generate(order_2)

payment_processor = PaymentProcessor()
payment_processor.process(order)
payment_processor.process(order_2)
