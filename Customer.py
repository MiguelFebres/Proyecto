class Customer:

  def __init__(self, Name_of_the_customer, customer_type, RIF, Gmail, shipment_address, phone_number):
    self.Name_of_the_customer = Name_of_the_customer
    self.customer_type = customer_type
    self.RIF = RIF
    self.Gmail = Gmail
    self.shipment_address = shipment_address
    self.phone_number = phone_number

  def showC(self):
    print(f'''
    Full name: {self.Name_of_the_customer}
    Customer juridic: {self.customer_type}
    RIF: {self.RIF}
    Gmail: {self.Gmail}
    Shipment address: {self.shipment_address}
    Phone number: {self.phone_number}
    ''')