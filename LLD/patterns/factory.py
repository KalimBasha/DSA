'''
Factory pattern solves which object to create.
Always write code and then trace for understanding the patterns.
'''

from abc import abstractmethod, ABC

class PaymentMethod(ABC):                    
    @abstractmethod
    def pay(self, amount: int):
        pass

class UPIPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paid ₹{amount} using UPI")

class CardPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paid ₹{amount} using Card")

class NetBankingPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paid ₹{amount} using NetBanking")

class CryptoPayment(PaymentMethod):          
    def pay(self, amount: int):
        print(f"Paid ₹{amount} using Crypto")

class PaymentFactory:
    __payment_methods = {
        "upi"        : UPIPayment,
        "card"       : CardPayment,
        "netbanking" : NetBankingPayment,
        "crypto"     : CryptoPayment,        
    }

    @staticmethod
    def get_payment_method(method: str) -> PaymentMethod:
        payment_class = PaymentFactory.__payment_methods.get(method)
        if not payment_class:
            raise ValueError(f"Invalid payment method: {method}")  # ✅ raise not print raise will break otherwise none class will be returned
        return payment_class()

def pay_amount(amount: int, method: str):
    payment_method = PaymentFactory.get_payment_method(method.lower())
    payment_method.pay(amount)

pay_amount(500, "upi")
pay_amount(1200, "card")
pay_amount(800, "crypto")

# TRACE: PaymentFactory.get_payment_method("card") is called
# Step 1 — goes to __payment_methods dictionary, looks up "card"
# Step 2 — finds CardPayment class (not instance — the blueprint)
# Step 3 — payment_class is not None, so no error raised
# Step 4 — returns CardPayment() — fresh instance created
# Step 5 — caller calls .pay(1200) on the CardPayment instance
# Output — "Paid ₹1200 using Card"