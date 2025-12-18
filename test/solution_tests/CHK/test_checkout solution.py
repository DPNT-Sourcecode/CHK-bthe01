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
        assert CheckoutSolution().checkout("AAAAABBEE") == int(310)

    def test_allAs(self):
        assert CheckoutSolution().checkout("AAAAAEEBAAABBFFF") == int(475)  

    def test_three_fs(self):
        assert CheckoutSolution().checkout("FFF") == int(20)
        assert CheckoutSolution().checkout("FFFF") == int(30)
        assert CheckoutSolution().checkout("FFFFFF") == int(40)

    def test_checkout_multi_offers(self):
        assert CheckoutSolution().checkout("VV") == int(90)
        assert CheckoutSolution().checkout("VVV") == int(130)
        assert CheckoutSolution().checkout("VVVV") == int(180)
        assert CheckoutSolution().checkout("VVVVV") == int(230)
        assert CheckoutSolution().checkout("VVVVVV") == int(260)

    def test_new_prodducts(self):
        assert CheckoutSolution().checkout("STXYZ") == int(200)
        assert CheckoutSolution().checkout("STXYSTX") == int(340)
        assert CheckoutSolution().checkout("PPPPP") == int(200)
        assert CheckoutSolution().checkout("QQQ") == int(80)
        

    

    def test_checkout_cross_item_offer(self):
        assert CheckoutSolution().checkout("EEB") == int(80)
        assert CheckoutSolution().checkout("EEEEBB") == int(160)
        assert CheckoutSolution().checkout("EEEB") == int(120)


