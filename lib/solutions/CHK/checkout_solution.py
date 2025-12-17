from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

@dataclass
class Offer:
    Quantity : int
    Price : int

@dataclass
class Prices:
    Item : str
    Price : int
    SpecialOffer : Optional[Offer] = None


class CheckoutSolution:

    def __init__(self):       
        self.prices = {
            'A': Prices(Item='A', Price=int('50'), SpecialOffer=Offer(Quantity=3, Price=int('130'))),
            'B': Prices(Item='B', Price=int('30'), SpecialOffer=Offer(Quantity=2, Price=int('45'))),
            'C': Prices(Item='C', Price=int('20')),
            'D': Prices(Item='D', Price=int('15')),
            'E': Prices(Item='E', Price=int('40')),
        }

    def getPrice(self, sku):
        return self.prices[sku].Price if sku in self.prices else None

    def checkSpecialOffer(self, sku, count):
        offer = self.prices[sku].SpecialOffer
        if offer and count >= offer.Quantity:
            num_offers = count // offer.Quantity
            remainder = count % offer.Quantity
            total_price = (num_offers * offer.Price) + (remainder * self.prices[sku].Price)
            return int(total_price)
        else:
            return int(count * self.prices[sku].Price)

    # skus = unicode string
    def checkout(self, skus):
        total = 0.0
        singularSkus = set(skus)

        
        for sku in singularSkus:
            if sku not in self.prices:
                return -1
            else:
                count = skus.count(sku)
                total += int(self.checkSpecialOffer(sku, count))

        return int(total)


