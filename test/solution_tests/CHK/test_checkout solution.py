from solutions.CHK.checkout_solution import CheckoutSolution    

class TestCheckoutSolution():
    def test_checkout_valid_skus_no_offers(self):
        assert CheckoutSolution().checkout("A") == 50

    def test_checkout_valid_skus_with_offers(self):
        assert CheckoutSolution().checkout("AAABBB") == 205

    def test_checkout_invalid_sku(self):
        assert CheckoutSolution().checkout("AABX") == -1