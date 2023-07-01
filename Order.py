class Order:

  def __init__(self, Customer_Name, Shipment_Date, Products_Taken, Order_Number):
    self.Customer_Name = Customer_Name
    self.Shipment_Date = Shipment_Date
    self.Product_Taken = Products_Taken
    self.Order_Number = Order_Number

  def showO(self):
    return f'''
    Customer: {self.Customer_Name}
    Shipment Date: {self.Shipment_Date}
    Products Taken: {self.Product_Taken}
    Order Number: {self.Order_Number}
    '''