def calculate_discount(price, discount_percent):
    discount = (discount_percent/100)*price
    finalPrice = price-discount
    if discount >= 20:
        return finalPrice
    else:
        return price





print(calculate_discount(200, 0))