class Sale:

  def __init__(self,customer, purchased_products, payment_method, shipment_method, total_payment, date):
    self.customer = customer
    self.purchased_products = purchased_products
    self.payment_method = payment_method
    self.shipment_method = shipment_method
    self.total_payment = total_payment
    self.date = date

  def showS(self):
    print(f'''
    Customer: {self.customer}
    Purchased Products: {self.purchased_products}
    Payment Method: {self.payment_method}
    Shipping Method: {self.shipment_method}
    Total Payment: {self.total_payment}
    Day: {self.date}
    ''')
    