from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self): pass

    @abstractmethod
    def pay(self, amount): pass

class RazorpayCardPayment(PaymentMethod):
    def __init__(self, card_number): self.card_number = card_number
    def get_details(self): return "Razorpay Card " + self.card_number
    def pay(self, amount):
        print("Paid", amount, "via", self.get_details())
        return True

class RazorpayUPIPayment(PaymentMethod):
    def __init__(self, upi_id): self.upi_id = upi_id
    def get_details(self): return "Razorpay UPI " + self.upi_id
    def pay(self, amount):
        print("Paid", amount, "via", self.get_details())
        return True

class StripeCardPayment(PaymentMethod):
    def __init__(self, card_number): self.card_number = card_number
    def get_details(self): return "Stripe Card " + self.card_number
    def pay(self, amount):
        print("Paid", amount, "via", self.get_details())
        return True

class StripeUPIPayment(PaymentMethod):
    def __init__(self, upi_id): self.upi_id = upi_id
    def get_details(self): return "Stripe UPI " + self.upi_id
    def pay(self, amount):
        print("Paid", amount, "via", self.get_details())
        return True

class FactoryPaymentMethod(ABC):
    factory = {}
    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        return cls.factory[method_type](**kwargs)

class RazorpayFactory(FactoryPaymentMethod):
    factory = {"card": RazorpayCardPayment, "upi": RazorpayUPIPayment}

class StripeFactory(FactoryPaymentMethod):
    factory = {"card": StripeCardPayment, "upi": StripeUPIPayment}

class Aggregator(ABC):
    def call_get_payment_object(self, method_type, amount, **kwargs):
        obj = self.payment_factory.get_payment_object(method_type, **kwargs)
        return obj.pay(amount)

class RazorpayAggregator(Aggregator):
    name = "Razorpay"
    processing_fee = 2.0
    payment_factory = RazorpayFactory

class StripeAggregator(Aggregator):
    name = "Stripe"
    processing_fee = 2.9
    payment_factory = StripeFactory

class AggregatorFactory:
    factory = {"stripe": StripeAggregator, "razorpay": RazorpayAggregator}
    @classmethod
    def get_aggregator_object(cls, aggregator_name):
        return cls.factory[aggregator_name]()

try:
    agg = AggregatorFactory.get_aggregator_object(input("Aggregator (stripe/razorpay): "))
    method = input("Method (card/upi): ")
    if method == "card":
        details = {"card_number": input("Card number: ")}
    else:
        details = {"upi_id": input("UPI ID: ")}
    amount = float(input("Amount: "))
    agg.call_get_payment_object(method, amount, **details)
except KeyError:
    print("Invalid choice")
