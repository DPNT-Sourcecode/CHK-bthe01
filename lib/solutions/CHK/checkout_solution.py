from dataclasses import dataclass
from typing import Optional, Sequence, Union
from decimal import Decimal

@dataclass
class multiOffer:
    Quantity : int
    Price : int
@dataclass
class buyXGetYFreeOffer:
    ItemToBuy : str
    ItemFree : str
    X : int
    Y : int

Offer = Union[multiOffer, buyXGetYFreeOffer]

@dataclass
class Prices:
    Item : str
    Price : int
    SpecialOffer : Sequence[Offer] = None





class CheckoutSolution:

    def __init__(self):       
        self.prices = {
            'A': Prices(Item='A', Price=int('50'), SpecialOffer=[multiOffer(Quantity=3, Price=int('130')), multiOffer(Quantity=5, Price=int('200'))]),
            'B': Prices(Item='B', Price=int('30'), SpecialOffer=[multiOffer(Quantity=2, Price=int('45'))]),
            'C': Prices(Item='C', Price=int('20')),
            'D': Prices(Item='D', Price=int('15')),
            'E': Prices(Item='E', Price=int('40'), SpecialOffer=[buyXGetYFreeOffer(ItemToBuy='E', ItemFree='B', X=2, Y=1)]),
        }

    def getPrice(self, sku):
        return self.prices[sku].Price if sku in self.prices else None

    def checkMultiOffer(self, sku, count, offer):
        if offer and count >= offer.Quantity:
            num_offers = count // offer.Quantity
            remainder = count % offer.Quantity
            total_price = (num_offers * offer.Price) + (remainder * self.prices[sku].Price)
            return int(total_price)
        else:
            return int(count * self.prices[sku].Price)
    
    def checkBuyXGetYFreeOffer(self, skus, sku, offer):
        if offer:
            item_to_buy = offer.ItemToBuy
            item_free = offer.ItemFree
            x = offer.X
            y = offer.Y

            num_eligible_offers = skus.count(item_to_buy) // x
            num_free_items = num_eligible_offers * y

        return num_free_items 
    
    def calculateFreeItems(self, item_free, num_free_items, skus):
        return int(max(0, skus.count(item_free) - num_free_items))

    # skus = unicode string
    def checkout(self, skus):
        total = 0.0
        singularSkus = set(skus)

        
        for sku in singularSkus:
            if sku not in self.prices:
                return -1
            else:
                count = skus.count(sku)
                if self.prices[sku].SpecialOffer:
                    for offer in self.prices[sku].SpecialOffer:
                        if isinstance(offer, buyXGetYFreeOffer):
                            countFree = 0
                            num_free_items = self.checkBuyXGetYFreeOffer(skus, sku, offer)
                            countFree -= self.calculateFreeItems(offer.ItemFree, num_free_items, skus)
                            total -= int(countFree * self.getPrice(offer.ItemFree))
                            total += int(self.getPrice(sku) * count)
                        elif isinstance(offer, multiOffer):
                            total += int(self.checkMultiOffer(sku, count, offer))
                    
                else:
                    total += int(count * self.prices[sku].Price)

        return int(total)





