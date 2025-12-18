from dataclasses import dataclass
from typing import List, Union
from collections import Counter
from loguru import logger

@dataclass(frozen=True)
class multiOffer:
    Quantity : int
    Price : int
@dataclass(frozen=True)
class buyXGetYFreeOffer:
    ItemToBuy : str
    ItemFree : str
    X : int
    Y : int

@dataclass(frozen=True)
class groupOffer:
    items : List[str]
    QuantityforEligibility : int
    Price : int

Offer = Union[multiOffer, buyXGetYFreeOffer]


@dataclass(frozen=True)
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
            'F': Prices(Item='F', Price=int('10'), Offers=[buyXGetYFreeOffer(ItemToBuy='F', ItemFree='F', X=2, Y=1)]),
            'G': Prices(Item='G', Price=int('20')),
            'H': Prices(Item='H', Price=int('10'), Offers=[multiOffer(Quantity=5, Price=int('45')), multiOffer(Quantity=10, Price=int('80'))]),
            'I': Prices(Item='I', Price=int('35')),
            'J': Prices(Item='J', Price=int('60')),
            'K': Prices(Item='K', Price=int('70'), Offers=[multiOffer(Quantity=2, Price=int('120'))]),
            'L': Prices(Item='L', Price=int('90')),
            'M': Prices(Item='M', Price=int('15')),
            'N': Prices(Item='N', Price=int('40'), Offers=[buyXGetYFreeOffer(ItemToBuy='N', ItemFree='M', X=3, Y=1)]),
            'O': Prices(Item='O', Price=int('10')),
            'P': Prices(Item='P', Price=int('50'), Offers=[multiOffer(Quantity=5, Price=int('200'))]),
            'Q': Prices(Item='Q', Price=int('30'), Offers=[multiOffer(Quantity=3, Price=int('80'))]),
            'R': Prices(Item='R', Price=int('50'), Offers=[buyXGetYFreeOffer(ItemToBuy='R', ItemFree='Q', X=3, Y=1)]),
            'S': Prices(Item='S', Price=int('20')),
            'T': Prices(Item='T', Price=int('20')),
            'U': Prices(Item='U', Price=int('40'), Offers=[buyXGetYFreeOffer(ItemToBuy='U', ItemFree='U', X=3, Y=1)]),
            'V': Prices(Item='V', Price=int('50'), Offers=[multiOffer(Quantity=2, Price=int('90')), multiOffer(Quantity=3, Price=int('130'))]),
            'W': Prices(Item='W', Price=int('20')),
            'X': Prices(Item='X', Price=int('17')),
            'Y': Prices(Item='Y', Price=int('20')),
            'Z': Prices(Item='Z', Price=int('21')),
        }

        self.groupOffers = [
            groupOffer(items=['S','T','X','Y','Z'], QuantityforEligibility=3, Price=int('45'))
        ]

    def applyGroupOffers(self, counts):
        groupTotal = 0
        for offer in self.groupOffers:
            eligibleItems = []
            for item in offer.items:
                eligibleItems += [item] * counts[item]
            
            checkPackages = len(eligibleItems) // offer.QuantityforEligibility
            if checkPackages == 0:
                continue
            # get the most expensive items first
            eligibleItems.sort(key=lambda x: self.priceCatalog[x].Price, reverse=True)
            # remove items used in group offer from counts
            itemsUsed = checkPackages * offer.QuantityforEligibility
            itemsUsedForPackages = eligibleItems[:itemsUsed]
            for sku in itemsUsedForPackages:
                counts[sku] -= 1
            
            # add group offer price to total
            groupTotal += checkPackages * offer.Price
        return groupTotal





    
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

                    if item_to_buy == item_free:
                        num_eligible_offers = counts[item_to_buy] // (x+y)
                        num_free_items = num_eligible_offers * y
                    else:
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

        # Apply cross item offers first to adjust counts
        self.applyCrossItemOffers(counts)
        # apply group offers next
        total = 0
        total += self.applyGroupOffers(counts)
        # finally apply multi offers and unit prices
        for sku, quantity in counts.items():
            total += self.getBestMultiOfferPrice(sku, quantity)



        return int(total)
