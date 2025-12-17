from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

@dataclass
class Offer:
    Quantity : int
    Price : Decimal

@dataclass
class Prices:
    Item : str
    Price : Decimal
    SpecialOffer : Optional[Offer] = None


class CheckoutSolution:

    def __init__(self):       
        self.prices = {
            'A': Prices(Item='A', Price=Decimal('50'), SpecialOffer=Offer(Quantity=3, Price=Decimal('130'))),
            'B': Prices(Item='B', Price=Decimal('30'), SpecialOffer=Offer(Quantity=2, Price=Decimal('45'))),
            'C': Prices(Item='C', Price=Decimal('20')),
            'D': Prices(Item='D', Price=Decimal('15')),
        }

    def getprice(self, sku):
        return self.prices[sku].Price if sku in self.prices else None

    def checkSpecialOffer(self, sku, count):
        offer = self.prices[sku].SpecialOffer
        if offer and count >= offer.Quantity:
            num_offers = count // offer.Quantity
            remainder = count % offer.Quantity
            total_price = (num_offers * offer.Price) + (remainder * self.prices[sku].Price)
            return total_price
        else:
            return count * self.prices[sku].Price

    # skus = unicode string
    def checkout(self, skus):
        total = 0.0
        singularSkus = set(skus)
        if len(singularSkus) == 1 and skus[0] in self.prices:
            return integer
        for sku in singularSkus:
            if sku not in self.prices:
                return -1
            else:
                count = skus.count(sku)
                total += float(self.checkSpecialOffer(sku, count))

        return total


