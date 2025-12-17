from solutions.CHK.checkout_solution import CheckoutSolution    

class TestCheckoutSolution():
    def test_checkout_valid_skus_no_offers(self):
        assert CheckoutSolution().checkout("ABCD") == 115.0

    def test_checkout_valid_skus_with_offers(self):
        assert CheckoutSolution().checkout("AAABBB") == 175.0

    def test_checkout_invalid_sku(self):
        assert CheckoutSolution().checkout("AABX") == -1