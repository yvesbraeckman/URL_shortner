def create_supplier(delay_factor, price_factor):
    def place_order(expected_delivery_time, price_estimate):
        adjusted_delivery_time = expected_delivery_time * delay_factor
        adjusted_price = price_estimate * price_factor
        print(f"geschatte levertijd: {int(adjusted_delivery_time)} dagen")
        print(f"geschatte kostprijs: {int(adjusted_price)} euro")
    return place_order

# Test code
get_offer_from_bol = create_supplier(0.8,1.1)
get_offer_from_amazon = create_supplier(1.2,0.9)
get_offer_from_aliexpress = create_supplier(1.5,0.75)


