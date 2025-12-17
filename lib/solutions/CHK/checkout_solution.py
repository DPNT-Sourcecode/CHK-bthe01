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

        

    # skus = unicode string
    def checkout(self, skus):

        raise NotImplementedError()

