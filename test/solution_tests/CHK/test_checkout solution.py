from solutions.CHK.checkout_solution import CheckoutSolution    

class TestCheckoutSolution():
    def test_checkout_valid_skus_no_offers(self):
        assert CheckoutSolution().checkout("ABCD") == int(115)

    def test_checkout_valid_skus_with_offers(self):
        assert CheckoutSolution().checkout("AAABBB") == int(205)

    def test_checkout_invalid_sku(self):
        assert CheckoutSolution().checkout("AABX") == -1

    def test_checkout_empty_string(self):
        assert CheckoutSolution().checkout("") == int(0)
    
    def test_checkout_only_offers(self):
        assert CheckoutSolution().checkout("AAAAABBBEE") == int(305)