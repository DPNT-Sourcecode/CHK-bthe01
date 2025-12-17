from dataclasses import dataclass
from typing import List, Optional, Sequence, Union
from decimal import Decimal
from collections import Counter
from loguru import logger

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
    Offers : List[Offer] = None





class CheckoutSolution:

    def __init__(self):       
        self.priceCatalog = {
            'A': Prices(Item='A', Price=int('50'), Offers=[multiOffer(Quantity=3, Price=int('130')), multiOffer(Quantity=5, Price=int('200'))]),
            'B': Prices(Item='B', Price=int('30'), Offers=[multiOffer(Quantity=2, Price=int('45'))]),
            'C': Prices(Item='C', Price=int('20')),
            'D': Prices(Item='D', Price=int('15')),
            'E': Prices(Item='E', Price=int('40'), Offers=[buyXGetYFreeOffer(ItemToBuy='E', ItemFree='B', X=2, Y=1)]),
        }


    
    def applyCrossItemOffers(self, counts):
        for item in self.priceCatalog.values():
            if not item.Offers:
                continue
            for offer in item.Offers:
                if isinstance(offer, buyXGetYFreeOffer):
                    item_to_buy = offer.ItemToBuy
                    item_free = offer.ItemFree
                    x = offer.X
                    y = offer.Y

                    num_eligible_offers = counts[item_to_buy] // x
                    num_free_items = num_eligible_offers * y

                    counts[item_free] = max(0, counts[item_free] - num_free_items)

    def getBestMultiOfferPrice(self, sku , quantity):
        item = self.priceCatalog[sku]
        unit_total = quantity * item.Price
        if not item.Offers:
            return unit_total
        multiOffers = [offer for offer in item.Offers if isinstance(offer, multiOffer)]
        if not multiOffers:
            return unit_total

        # using dynamic programming to find the best combination of offers
        dp = [float('inf')] * (quantity + 1)
        dp[0] = 0
        for x in range(1, quantity +1):
            for offer in multiOffers:
                if x >= offer.Quantity:
                    dp[x] = min(dp[x], dp[x - offer.Quantity] + offer.Price)
            dp[x] = min(dp[x], dp[x -1] + item.Price)
            
        return dp[quantity]


    # skus = unicode string
    def checkout(self, skus):
        total = 0.0
        singularSkus = set(skus)
        for sku in singularSkus:
            if sku not in self.priceCatalog:
                return -1
            
        counts = Counter(skus)
        
        self.applyCrossItemOffers(counts)

        total = 0

        for sku, quantity in counts.items():
            total += self.getBestMultiOfferPrice(sku, quantity)



        return int(total)

