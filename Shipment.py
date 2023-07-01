from Order import Order

class Shipment:

  def __init__(self, Order_Number, Shipment_Service, Shipment_Price):
    self.Order_Number = Order_Number
    self.Shipment_Service = Shipment_Service
    self.Shipment_Price = Shipment_Price

  def showShip(self):
    return f'''
    Order Number: {self.Order_Number}
    Shipment Service: {self.Shipment_Service}
    Shipment Price: {self.Shipment_Price}
    '''