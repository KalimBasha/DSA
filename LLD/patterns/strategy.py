'''
Build a Zepto sorting system. Products can be sorted by:

Price low to high
Price high to low
Ratings (highest first)
Delivery time (fastest first)

Write:

Abstract SortStrategy with sort(products: list) -> list
Four concrete strategies
ProductSorter context class with set_strategy() and sort()
SortStrategyFactory with dictionary lookup
A Product class with name, price, rating, delivery_time
Calling code — list of 4 products, sorted four different ways
Trace at bottom
'''


from abc import ABC, abstractmethod

# Abstract Strategy
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, products: list) -> list:
        pass

# Concrete Strategies
class PriceAscending(SortStrategy):
    def sort(self, products: list) -> list:
        return sorted(products, key=lambda p: p.price)

class PriceDescending(SortStrategy):
    def sort(self, products: list) -> list:
        return sorted(products, key=lambda p: p.price, reverse=True)

class RatingHighest(SortStrategy):
    def sort(self, products: list) -> list:
        return sorted(products, key=lambda p: p.rating, reverse=True)

class DeliveryFastest(SortStrategy):
    def sort(self, products: list) -> list:
        return sorted(products, key=lambda p: p.delivery_time)

# Context
class ProductSorter:
    def __init__(self, strategy: SortStrategy):
        self.__strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.__strategy = strategy

    def get_sorted_list(self, products: list) -> list:
        return self.__strategy.sort(products)

# Factory
class SortStrategyFactory:
    __methods = {
        "price-asc"     : PriceAscending,
        "price-desc"    : PriceDescending,
        "ratings"       : RatingHighest,
        "delivery-fast" : DeliveryFastest,
    }

    @staticmethod
    def get_strategy(method: str) -> SortStrategy:
        strategy_class = SortStrategyFactory.__methods.get(method.lower())
        if not strategy_class:
            raise ValueError(f"Invalid method: {method}")
        return strategy_class()

# Product
class Product:
    def __init__(self, name: str, price: float,
                 rating: float, delivery_time: int):
        self.name = name
        self.price = price
        self.rating = rating
        self.delivery_time = delivery_time

    def __str__(self):
        return (f"{self.name} | ₹{self.price} | "
                f"⭐{self.rating} | {self.delivery_time}min")

# Calling code
products = [
    Product("Milk", 60.0, 4.2, 15),
    Product("Bread", 40.0, 4.5, 10),
    Product("Eggs", 90.0, 4.8, 20),
    Product("Butter", 55.0, 4.1, 8),
]

sorter = ProductSorter(SortStrategyFactory.get_strategy("price-asc"))
print("Price Low → High:")
for p in sorter.get_sorted_list(products):
    print(" ", p)

sorter.set_strategy(SortStrategyFactory.get_strategy("price-desc"))
print("\nPrice High → Low:")
for p in sorter.get_sorted_list(products):
    print(" ", p)

sorter.set_strategy(SortStrategyFactory.get_strategy("ratings"))
print("\nRatings Highest First:")
for p in sorter.get_sorted_list(products):
    print(" ", p)

sorter.set_strategy(SortStrategyFactory.get_strategy("delivery-fast"))
print("\nFastest Delivery First:")
for p in sorter.get_sorted_list(products):
    print(" ", p)

# TRACE: SortStrategyFactory.get_strategy("ratings") then sorter.get_sorted_list(products)
# Step 1 — get_strategy("ratings") → looks up "ratings" in __methods dict
# Step 2 — finds RatingHighest class → calls RatingHighest() → returns instance
# Step 3 — sorter.set_strategy(RatingHighest instance) → __strategy updated
# Step 4 — get_sorted_list(products) → calls self.__strategy.sort(products)
# Step 5 — RatingHighest.sort() → sorted(products, key=lambda p: p.rating, reverse=True)
# Step 6 — returns new sorted list, highest rating first → [Eggs⭐4.8, Bread⭐4.5, Milk⭐4.2, Butter⭐4.1]