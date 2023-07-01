class Paycheck:

  def __init__(self, Paid_By, Total_Sale, Payment_Currency, Type_of_Payment, Payment_Date):
    self.Paid_By = Paid_By
    self.Total_Sale = Total_Sale
    self.Payment_Currency = Payment_Currency
    self.Type_of_Payment = Type_of_Payment
    self.Payment_Date = Payment_Date

  def showPay(self):
    return f'''
    Customer: {self.Paid_By}
    Total Paid: {self.Total_Sale}
    Payment Currency: {self.Payment_Currency}
    Type of Payment: {self.Type_of_Payment}
    Payment Date: {self.Payment_Date}
    '''