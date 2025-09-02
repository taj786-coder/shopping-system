def calculate_bill(cart):
    subtotal = sum(price for _, _, _, _, price in cart)
