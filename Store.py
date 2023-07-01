from Product import Product
from Sale import Sale
# # from Statistics import Statistics 
from Shipment import Shipment
from Paycheck import Paycheck
from Customer import Customer 
from Bill import Bill 
from Order import Order 

class Store:
  
    def __init__(self, products, new_products, customers, sales, pagos, orders, shipments):
      self.products = products
      self.new_products = []
      self.customers = []
      self.sales = []
      self.pagos = []
      self.orders = []
      self.shipments = []
      
    def initial_products(self):
      for Dicc in self.products:
        Name_of_the_product = Dicc['name']
        Description = Dicc['description']
        Price = Dicc['price']
        Category = Dicc['category']
        Stock=Dicc['quantity']
        initial_product = Product(Name_of_the_product, Description, Price, Category,Stock)
        self.new_products.append(initial_product)   
        
    def ShowSt(self):
     for products in range(len(self.new_products)):
        print(f'{products +1}.{self.new_products[products].showP()}')
       
    def add_products(self):
      Name_of_the_product = input('Ingrese el nombre del producto: ')
      while Name_of_the_product == '':
        Name_of_the_product = input('INGRESE un nombre para el producto: ')
      Name_of_the_product = Name_of_the_product.capitalize()
      Description = input('Ingrese la descripción del producto: ')
      Price = input('Ingrese el precio del producto: ')
      while not Price.isnumeric():
        Price = input('Error! ingrese un precio valido: ')
      Category = input('Ingrese la categoria del producto: ')
      while not Category.isalpha():
        Category = input('Error! las categorias no pueden llevar numeros, reingrese la categoria del producto')
      Category = Category.capitalize()
      last_added_product = Product(Name_of_the_product, Description, Price, Category)
      self.new_products.append(last_added_product)
      
    def search_products_name(self):
      Name_of_the_product = input('Ingrese el nombre del producto que desea buscar: ')
      Name_of_the_product = Name_of_the_product.split()
      for j in range(len(Name_of_the_product)):
        Name_of_the_product[j] = Name_of_the_product[j].capitalize()
      Name_of_the_product = ' '.join(Name_of_the_product)
      found=False
      for names in self.new_products:
        
        if names.Name_of_the_product==Name_of_the_product:
          print(names.showP())
          found=True
      if found==False:
        print('Papi no esta')
        
    def search_products_category(self):
      Category_of_the_product = input('Ingrese la categoria del producto que desea buscar: ')
      Category_of_the_product = Category_of_the_product.split()
      for j in range(len(Category_of_the_product)):
        Category_of_the_product[j] = Category_of_the_product[j].capitalize()
      Category_of_the_product = ' '.join(Category_of_the_product)
      found=False
      for categories in self.new_products:
        
        if categories.Category==Category_of_the_product:
          print(categories.showP())
          found=True
      if found==False:
        print('Papi no esta')
        
    def search_products_price(self):
      Price = input('Ingrese el precio del producto que desea buscar: ')
      while not Price.isnumeric():
        Price = input('Error! Ingrese un precio numerico: ')
      found=False
      for prices in self.new_products:
        if prices.Price==int(Price):
          print(prices.showP())
          found=True
      if found==False:
        print('Papi no esta')
        
    def search_products_quantity(self):
      quantity = input('Ingrese la cantidad en el inventario del producto que desea buscar: ')
      while not quantity.isnumeric():
        quantity = input('Error! Ingrese un precio numerico: ')
      found=False
      for quantities in self.new_products:
        if quantities.Stock==int(quantity):
          print(quantities.showP())
          found=True
      if found==False:
        print('Papi no esta')
        
    def modify_products(self):
      Name_of_the_product = input('Ingrese el nombre del producto que desea modificar: ')
      Name_of_the_product = Name_of_the_product.split()
      for j in range(len(Name_of_the_product)):
        Name_of_the_product[j] = Name_of_the_product[j].capitalize()
      Name_of_the_product = ' '.join(Name_of_the_product)
      
      found=False
      for names in self.new_products:
        
        if names.Name_of_the_product==Name_of_the_product:
          names.Name_of_the_product = input('Ingrese un nuevo nombre para el producto: ')
          while names.Name_of_the_product == '':
            names.Name_of_the_product = input('INGRESE un nombre para el producto: ')
          names.Name_of_the_product = names.Name_of_the_product.capitalize()
          names.Description = input('Ingrese la descripción del producto: ')
          names.Price = input('Ingrese el precio del producto: ')
          while not names.Price.isnumeric():
            names.Price = input('Error! ingrese un precio valido: ')
          names.Category = input('Ingrese la categoria del producto: ')
          while not names.Category.isalpha():
            names.Category = input('Error! las categorias no pueden llevar numeros, reingrese la categoria del producto')
          names.Category = names.Category.capitalize()
          found=True
          if found==False:
            print('Papi no esta lo que desea modificar')
            
    def delete_products(self):
      Name_of_the_product = input('Ingrese el nombre del producto que desea eliminar: ')
      Name_of_the_product = Name_of_the_product.split()
      for j in range(len(Name_of_the_product)):
        Name_of_the_product[j] = Name_of_the_product[j].capitalize()
      Name_of_the_product = ' '.join(Name_of_the_product)
      found=False
      for names in range(len(self.new_products)):
        
        if self.new_products[names].Name_of_the_product==Name_of_the_product:
          self.new_products.pop(names)
          found=True
      if found==False:
        print('Papi no esta')
        
    def register_customer(self):
      Name_of_the_customer = input('Ingrese el nombre completo del cliente o razon social : ')
      while Name_of_the_customer == '':
        Name_of_the_customer = input('INGRESE el nombre completo del cliente o razon social : ')
      Name_of_the_customer = Name_of_the_customer.split()
      for j in range(len(Name_of_the_customer)):
        Name_of_the_customer[j] = Name_of_the_customer[j].capitalize()
      Name_of_the_customer = ' '.join(Name_of_the_customer)
      type_of_the_customer_juridico=True
      ops=input('Si el cliente es juridico presione 1, si el cliente es natural presione 2: ')
      while not (ops=='1' or  ops=='2'):
        ops=input('Ingrese una opcion valida ')
      if ops=='2':
        type_of_the_customer_juridico=False
      rif=input('Ingrese la cedula ')
      while not rif.isnumeric() or len(rif)>8:
        rif=input('Ingrese una cedula valida ')
      gmail=input('Ingrese su gmail ')
      while not ('@gmail.com' in gmail) or len(gmail)<11:
        gmail=input('Ingrese su gmail, recuerde que debe tener @gmail.com en su correo ')
      shippment_adress=input('Ingrese su direccion ')
      phone=input('Ingrese el numero de telefono ')
      while not phone.isnumeric() or not len(phone)==11:
        phone=input('Ingrese un numero valido recuerde debe tener 11 digitos , como en el siguiente ejemplo 04126216153 ')
      new_costumer=Customer(Name_of_the_customer, type_of_the_customer_juridico, rif, gmail, shippment_adress, phone)
      self.customers.append(new_costumer)
      
    def modify_customer(self):
      Name_of_the_customer = input('Ingrese el nombre del cliente que desea modificar: ')
      Name_of_the_customer = Name_of_the_customer.split()
      for j in range(len(Name_of_the_customer)):
        Name_of_the_customer[j] = Name_of_the_customer[j].capitalize()
      Name_of_the_customer = ' '.join(Name_of_the_customer)
      found=False
      for names in self.customers:
        if names.Name_of_the_customer==Name_of_the_customer:
          names.Name_of_the_customer = input('Ingrese el nombre completo del cliente o razon social : ')
          while names.Name_of_the_customer == '':
            names.Name_of_the_customer = input('INGRESE el nombre completo del cliente o razon social : ')
          Name_of_the_customer = Name_of_the_customer.split()
          for j in range(len(Name_of_the_customer)):
              Name_of_the_customer[j] = Name_of_the_customer[j].capitalize()
          Name_of_the_customer = ' '.join(Name_of_the_customer)
          names.type_of_the_customer_juridico=True
          ops=input('Si el cliente es juridico presione 1, si el cliente es natural presione 2: ')
          while not (ops=='1' or  ops=='2'):
            ops=input('Ingrese una opcion valida ')
          if ops=='2':
            names.type_of_the_customer_juridico=False
          names.rif=input('Ingrese la cedula ')
          while not names.rif.isnumeric() or len(names.rif)>8:
            names.rif=input('Ingrese una cedula valida ')
          names.gmail=input('Ingrese su gmail ')
          while not '@gmail.com' in names.gmail:
            names.gmail=input('Ingrese su gmail, recuerde que debe tener @gmail.com en su correo ')
          names.shippment_adress=input('Ingrese su direccion ')
          names.phone=input('Ingrese el numero de telefono ')
          while not names.phone.isnumeric() or not len(names.phone)==11:
            names.phone=input('Ingrese un numero valido recuerde debe tener 11 digitos , como en el siguiente ejemplo 04126216153 ')
            found=True
        if found==False:
         print('Papi no esta') 
          
    def delete_customer(self):
      Name_of_the_customer = input('Ingrese el nombre del cliente que desea eliminar: ')
      Name_of_the_customer = Name_of_the_customer.split()
      for j in range(len(Name_of_the_customer)):
        Name_of_the_customer[j] = Name_of_the_customer[j].capitalize()
      Name_of_the_customer = ' '.join(Name_of_the_customer)
      found=False
      for names in range(len(self.customers)):
        if self.customers[names].Name_of_the_customer==Name_of_the_customer:
          self.customers.pop(names)
          found=True
      if found==False:
        print('Papi no esta')
        
    def search_customers_rif(self):
      Rif = input('Ingrese la cedula o rif  del cliente que desea buscar: ')
      while not Rif.isnumeric():
        Rif = input('Error! Ingrese un RIF numerico: ')
      found=False
      for rifs in self.customers:
        if rifs.RIF==(Rif):
          print(rifs.showC())
          found=True
      if found==False:
        print('Papi no esta')
        
    def search_customers_gmail(self):
      Gmail = input('Ingrese el correo del cliente que desea buscar: ')
      while not '@gmail.com' in Gmail or len(Gmail)<10:
        Gmail = input('Error! Ingrese un gmail para la busqueda, recuerde que debe incluir @gmail.com: ')
      found=False
      for gmails in self.customers:
        if gmails.Gmail==Gmail:
          print(gmails.showC())
          found=True
      if found==False:
        print('Papi no esta')
        
    def register_sales(self):
      if len(self.customers)==0:
        print('No hay clientes registrados por favor registrelos ')
        self.register_customer()
        
      Rif = input('Ingrese la cedula o rif  del cliente: ')
      while not Rif.isnumeric():
        Rif = input('Error! Ingrese un RIF numerico: ')
      found=False
      for rifs in self.customers:
        if rifs.RIF==(Rif):
          found=True
          costumer_bought = rifs.Name_of_the_customer
          juridic = rifs.customer_type
        elif rifs.RIF!=Rif:
          print('El cliente no esta registrado por favor registrelo')
          self.register_customer()
          costumer_bought = rifs.Name_of_the_customer
          juridic = rifs.customer_type
      products_bought = []
      Price_1 = 0 
      sub_total=0
      optionss=0
      while not optionss=='1':
        product_bought={}
        optionss = input('Ingrese el nombre del producto comprado o coloque 1 para no colocar mas: ')
        if optionss=='1':
          break
        opptions = input('Ingrese la cantidad comprada de cada producto: ')
        while not optionss != '':
          optionss = input('INGRESE el nombre del producto comprado: ')
        while not (opptions.isnumeric() or opptions != ''):
          opptions = input('INGRESE la cantidad comprada de cada producto: ') 
        optionss = optionss.split()
        for j in range(len(optionss)):
          optionss[j] = optionss[j].capitalize()
        optionss = ' '.join(optionss)
        for products in range(len(self.new_products)):
          if self.new_products[products].Name_of_the_product==optionss:
            Price_1=self.new_products[products].Price
            product_bought[optionss]=opptions
            products_bought.append(product_bought)
        sub_total += (Price_1*(int(opptions)))
      
      options_1_1_1=['PdV','Cash','PM','Zelle']
      for index_ops_1_1_1 in range(len(options_1_1_1)):
        print(f'''{index_ops_1_1_1+1}.{options_1_1_1[index_ops_1_1_1]}''')
      option_1_1_1=input('Ingrese la opción de pago: ')
      while not option_1_1_1.isnumeric() or not int(option_1_1_1)-1 in range(len(options_1_1_1)):
        option_1_1_1=input('Error! Ingrese un numero dentro de las opciones ')
      date = input('Ingrese la fecha , tome de ejemplo: 16/04/23: ')
      while not date != '' or date.isnumeric() or range(len(date)) == 6:
        date = input('INGRESE la fecha , tome de ejemplo: 16/04/23: ')
      Type_of_payment=options_1_1_1[int(option_1_1_1)-1]
      options_1_1_2=['Zoom','Delivery','MRW','No papi']
      for index_ops_1_1_2 in range(len(options_1_1_2)):
         print(f'''{index_ops_1_1_2+1}.{options_1_1_2[index_ops_1_1_2]}''')
      option_1_1_2=input('Ingrese la opción de delivery: ')
      while not option_1_1_2.isnumeric() or not int(option_1_1_2)-1 in range(len(options_1_1_2)):
        option_1_1_2=input('Error! Ingrese un numero dentro de las opciones ')
      if option_1_1_2=='1' or option_1_1_2=='2' or option_1_1_2=='3':
        Order_Number = input('Ingrese el numero de la orden, debe de ser de mas de 3 digitos: ')
        while not (Order_Number != '' or Order_Number.isnumeric() or range(len(Order_Number)) == 3 ):
          Order_Number = input('INGRESE el numero de la orden, debe de ser de mas de 3 digitos: ')
      orden = Order(costumer_bought, date, products_bought, Order_Number)
      self.orders.append(orden)
      Type_of_shipment = options_1_1_2[int(option_1_1_2)-1]  
      total_payment = sub_total
      discount=0
      IGTF=0
      if juridic==True:
        discount=total_payment*(5/100)
      IVA=total_payment*(16/100)
      if option_1_1_1=='2':
        IGTF=total_payment*(3/100)
      total_payment=total_payment-discount+IVA+IGTF
      bill = Bill(sub_total, discount, IVA, IGTF, total_payment)
      sales=Sale(costumer_bought, products_bought, Type_of_payment,Type_of_shipment,total_payment,date)
      self.sales.append(sales)
      options_1_3=['Si','NO']
      for index_ops_1_3 in range(len(options_1_3)):
        print(f'''{index_ops_1_3+1}.{options_1_3[index_ops_1_3]}''')
      option_1_3=input('des: ')
      while not option_1_3.isnumeric() or not int(option_1_3)-1 in range(len(options_1_3)):
        option_1_3=input('Error! Ingrese un numero dentro de las opciones ')
      if option_1_3=='1':
        print(bill.showB())
        print(f'''    Order Number: {Order_Number}''')
        if juridic==True:
          print('''
          puede pagar dentro de 15 a 30 dias
          ''') 
          
    def search_sale_date(self):
      Date_1 = input('Ingrese la fecha de la venta que desea buscar: ')
      while not (Date_1 != '' or Date_1.isnumeric() or range(len(Date_1))==6):
        Date_1 = input('Error! Ingrese una fecha valida: ')
      found = False
      for dates in self.sales:
        if dates.date == Date_1:
          return dates.showS()
          found = True
      if found == False:
        print('Papi no esta')

    def search_sale_customer(self):
      Sale_Rif = input('Ingrese la cedula del cliente de la venta que desea buscar: ')
      while not (Sale_Rif != '' or Sale_Rif.isnumeric()):
        Sale_Rif = input('Error! Ingrese una cedula valida: ')
      found = False
      for Rifz in self.sales:
        if Rifz.customer == Sale_Rif:
          return Rifz.showS()
          found = True
      if found == False:
        print('Papi no esta')

    def search_sale_total_amount(self):
      Total_Sale = int(input('Ingrese el monto total de la venta que desea buscar: '))
      while not (Total_Sale != '' or Total_Sale.isnumeric()):
        Total_Sale = int(input('Error! Ingrese un monto numerico valido: '))
      found = False
      for Totalz in self.sales:
        if int(Totalz.total_payment) == int(Total_Sale):
          return Totalz.showS()
          found = True
      if found == False:
        print('Papi no esta')

    def register_paycheck(self):
      if len(self.sales) == 0:
        print('No hay ventas registradas por favor registrelas ')
        self.register_sales()

      Rif = input('Ingrese la cedula o rif  del cliente: ')
      while not Rif.isnumeric():
        Rif = input('Error! Ingrese un RIF numerico: ')
      found=False
      for rifs in self.customers:
        if rifs.RIF==(Rif):
          found = True
        elif rifs.RIF!=Rif:
          print('El cliente no esta registrado por favor registrelo')
          self.register_customer()  
      Total_Sale = int(input('Ingrese el monto total de la venta a pagar: '))
      while not (Total_Sale != '' or Total_Sale.isnumeric()):
        Total_Sale = int(input('Error! Ingrese un monto numerico valido: '))
      found = False
      for Totalz in self.sales:
        if int(Totalz.total_payment) == int(Total_Sale):
          found = True
      if found == False:
        while not (int(Totalz.total_payment) == int(Total_Sale) or Total_Sale.isnumeric() or Total_Sale != ''):
          Total_Sale = input('INGRESE el monto total de la venta a pagar: ')
      Payment_Currency = input('Ingrese el tipo de moneda con la que va a realizar el pago: ')
      while not (Payment_Currency != '' or Payment_Currency.isalpha()):
        Payment_Currency = input('INGRESE el tipo de moneda con la que va a realizar el pago: ')
      Type_of_payment_1 = input('Ingrese la forma de pago que planea utilizar: ')
      while not (Type_of_payment_1 != '' or Type_of_payment_1.isalpha()):
        Type_of_payment_1 = input('INGRESE la forma de pago que planea utilizar: ')
      Payment_Date = input('Ingrese la fecha del pago: ')
      while not (Payment_Date != '' or Payment_Date.isnumeric() or range(len(Payment_Date))==6):
         Payment_Date = input('INGRESE la fecha del pago: ')
      Pagos = Paycheck(Rif, Total_Sale, Payment_Currency, Type_of_payment_1, Payment_Date)
      self.pagos.append(Pagos)

    def search_paycheck_customer(self):
      Paycheck_Rif = input('Ingrese la cedula del cliente del pago que desea buscar: ')
      while not (Paycheck_Rif != '' or Paycheck_Rif.isnumeric()):
        Paycheck_Rif = input('Error! Ingrese una cedula valida: ')
      found = False
      for Rifx in self.pagos:
        if Rifx.Paid_By == Paycheck_Rif:
          print(Rifx.showPay())
          found = True
      if found == False:
        print('Papi no esta')

    def search_paycheck_date(self):
      Date_2 = input('Ingrese la fecha del pago que desea buscar: ')
      while not (Date_2 != '' or Date_2.isnumeric() or range(len(Date_2))==6):
        Date_2 = input('Error! Ingrese una fecha valida: ')
      found = False
      for datez in self.pagos:
        if datez.Payment_Date == Date_2:
          print(datez.showPay())
          found = True
      if found == False:
        print('Papi no esta')

    def search_paycheck_type_of_payment(self):
      Type_of_Payment_3 = input('Ingrese la forma de pago en la que se realizo el pago que busca: ')
      while not (Type_of_Payment_3 != '' or Type_of_Payment_3.isalpha()):
        Type_of_Payment_3 = input('INGRESE la forma de pago en la que se realizo el pago que busca: ')
      found = False
      for Tpayment in self.pagos:
        if Tpayment.Type_of_Payment == Type_of_Payment_3:
          print(Tpayment.showPay())
          found = True
        if found == False:
          print('Papi no esta')

    def search_paycheck_currency_type(self):
      Payment_Currency_3 = input('Ingrese la moneda en la que se realizo el pago que busca: ')
      while not (Payment_Currency_3 != '' or Payment_Currency_3.isalpha()):
        Payment_Currency_3 = input('INGRESE la moneda en la que se realizo el pago que busca: ')
      found = False
      for paymentC in self.pagos:
        if paymentC.Payment_Currency == Payment_Currency_3:
          print(paymentC.showPay())
          found = True
        if found == False:
          print('Papi no esta')

    def register_shipment(self):
      if len(self.sales) == 0:
        print('No hay ventas registradas por favor registrelas ')
        self.register_sales()
      
      
      Datos_Delivery = ''
      Order_number_1 = input('Ingrese el numero del orden de compra de la venta que desea registrarle un envio: ')
      while not (Order_number_1 != '' or Order_number_1.isnumeric() or range(len(Order_number_1)) == 3 ):
        Order_number_1 = input('INGRESE el numero del orden de compra de la venta que desea registrarle un envio: ')
      found = False
      for OrderN in self.orders:
        if OrderN.Order_Number == Order_number_1:
          print('''
        
        Escriba la opcion de envío para esta compra, tenemos disponibles las siguientes opciones de envio:
        Zoom
        Delivery
        MRW
        ''')
        Shipment_Service = input('Su eleccion es: ')
        while not (Shipment_Service != '' or Shipment_Service == 'Zoom' or Shipment_Service == 'Delivery' or Shipment_Service == 'MRW'):
          Shipment_Service = input('Ingrese una opcion valida dentro de las anteriormente mencionadas: ')
        Shipment_Price = input('Ingrese el precio del envio: ')
        if Shipment_Service == 'Delivery':
          Datos_Delivery = input('Ingrese los datos del motorizado: ')
        shipping = Shipment(Order_number_1, Shipment_Service, Shipment_Price)
        self.shipments.append(shipping)
        print(OrderN.showO())
        print(shipping.showShip())
        print(f'''    Datos del delivery: {Datos_Delivery}
        
        ''')
        found = True
        if found == False:
          print('Papi no esta')

    def search_shipment_customer(self):
      Shipment_Rif = input('Ingrese la cedula del cliente del pago que desea buscar: ')
      while not (Shipment_Rif != '' or Shipment_Rif.isnumeric()):
        Shipment_Rif = input('Error! Ingrese una cedula valida: ')
      found = False
      for Rifw in self.orders:
        if Rifw.Customer_Name == Shipment_Rif:
          print(Rifw.showO())
          print(Rifw.showShip())
          found = True
      if found == False:
        print('Papi no esta')



    def menu(self):
      
     while True:
     
      options=['Gestionar Productos','Gestionar ventas','Gestionar Clientes','Gestionar Pagos','Gestionar envios','Gestionar Estadísticas','Salir']
      for index_ops in range(len(options)):
        print(f'''{index_ops+1}.{options[index_ops]}''')
      option=input('Ingrese la opción deseada: ')
      while not option.isnumeric() or not int(option)-1 in range(len(options)):
        option=input('Error! Ingrese un numero dentro de las opciones ')
       
      if option=='1':
       
        options_1=['Agregar Productos','Buscar Productos','Modificar Productos','Eliminar Productos','Atras']
        for index_ops_1 in range(len(options_1)):
          print(f'''{index_ops_1+1}.{options_1[index_ops_1]}''')
        option_1=input('Ingrese la opción deseada: ')
        while not option_1.isnumeric() or not int(option_1)-1 in range(len(options_1)):
          option_1=input('Error! Ingrese un numero dentro de las opciones ')
        if option_1=='1':
         self.add_products()

        elif option_1=='2':
          options_1_1=['Buscar por nombre','Buscar por categoria','Buscar por precio','Buscar por disponibilidad','Salir']
          for index_ops_1_1 in range(len(options_1_1)):
            print(f'''{index_ops_1_1+1}.{options_1_1[index_ops_1_1]}''')
          option_1_1=input('Ingrese la opción deseada: ')
          while not option_1_1.isnumeric() or not int(option_1_1)-1 in range(len(options_1_1)):
            option_1_1=input('Error! Ingrese un numero dentro de las opciones ')
          if option_1_1=='1':
            self.search_products_name()
          elif option_1_1=='2':
            self.search_products_category()
          elif option_1_1=='3':
            self.search_products_price()
          elif option_1_1=='4':
            self.search_products_quantity()
          else:
            self.menu()
          
            
        elif option_1=='3':
          self.modify_products()

        elif option_1=='4':
          self.delete_products()

        else:
          break

      elif option == '2':
        options_2 = ['Registrar ventas','Buscar Venta','Atras']
        for index_ops_2 in range(len(options_2)):
          print(f'''{index_ops_2+1}.{options_2[index_ops_2]}''')
        option_2 = input('Ingrese la opción deseada: ')
        while not option_2.isnumeric() or not int(option_2)-1 in range(len(options_2)):
          option_2=input('Error! Ingrese un numero dentro de las opciones ')
        if option_2 == '1':
         self.register_sales()

        elif option_2 == '2':
          options_4 = ['Buscar por fecha','Buscar por cliente','Buscar por monto total de la venta', 'Atras']
          for index_ops_4 in range(len(options_4)):
            print(f'''{index_ops_4+1}.{options_4[index_ops_4]}''')
          option_4 = input('Ingrese la opción deseada: ')
          while not option_4.isnumeric() or not int(option_4)-1 in range(len(options_4)):
            option_4 = input('Error! Ingrese un numero dentro de las opciones ')
          if option_4 == '1':
           self.search_sale_date()

          elif option_4 == '2':
            self.search_sale_customer()

          elif option_4 == '3':
            self.search_sale_total_amount()

          else:
            self.menu()
        
        else:
          self.menu()
         
      elif option=='3':
          options_3=['Resgistrar Clientes','Modificar Informacion de clientes','Eliminar clientes','Buscar clientes','Atras']
          for index_ops_3 in range(len(options_3)):
            print(f'''{index_ops_3+1}.{options_3[index_ops_3]}''')
          option_3=input('Ingrese la opción deseada: ')
          while not option_3.isnumeric() or not int(option_3)-1 in range(len(options_3)):
            option_3=input('Error! Ingrese un numero dentro de las opciones ')
          if option_3=='1':
            self.register_customer()

          elif option_3=='2':
            self.modify_customer()

          elif option_3=='3':
            self.delete_customer()

          elif option_3=='4':
            options_3_1=['Buscar por Rif','Buscar por gmail','Salir']
            for index_ops_3_1 in range(len(options_3_1)):
              print(f'''{index_ops_3_1+1}.{options_3_1[index_ops_3_1]}''')
            option_3_1=input('Ingrese la opción deseada: ')
            while not option_3_1.isnumeric() or not int(option_3_1)-1 in range(len(options_3_1)):
              option_3_1=input('Error! Ingrese un numero dentro de las opciones ')
            if option_3_1=='1':
              self.search_customers_rif()
            elif option_3_1=='2':
              self.search_customers_gmail()
            else:
              break

          else:
            break
       
      elif option=='4':
        options_4=['Registrar pagos','Buscar pagos','Atras']
        for index_ops_4 in range(len(options_4)):
          print(f'''{index_ops_4+1}.{options_4[index_ops_4]}''')
        option_4=input('Ingrese la opción deseada: ')
        while not option_4.isnumeric() or not int(option_4)-1 in range(len(options_4)):
          option_4=input('Error! Ingrese un numero dentro de las opciones ')
        if option_4=='1':
         self.register_paycheck()

        elif option_4 == '2':
          options_9 = ['Buscar por clientes','Buscar por fechas','Buscar por tipo de pago', 'Buscar por moneda de pago', 'Atras']
          for index_ops_9 in range(len(options_9)):
            print(f'''{index_ops_9+1}.{options_9[index_ops_9]}''')
          option_9 = input('Ingrese la opción deseada: ')
          while not option_9.isnumeric() or not int(option_9)-1 in range(len(options_9)):
            option_9 = input('Error! Ingrese un numero dentro de las opciones ')
          if option_9 == '1':
            self.search_paycheck_customer()
          elif option_9 == '2':
            self.search_paycheck_date()
          elif option_9 == '3':
            self.search_paycheck_type_of_payment()
          elif option_9 == '4':
            self.search_paycheck_currency_type()
          else:
            self.menu()
       
      elif option=='5':
        options_5=['Registrar envios','Buscar envios','Atras']
        for index_ops_5 in range(len(options_5)):
          print(f'''{index_ops_5+1}.{options_5[index_ops_5]}''')
        option_5=input('Ingrese la opción deseada: ')
        while not option_5.isnumeric() or not int(option_5)-1 in range(len(options_5)):
          option_5=input('Error! Ingrese un numero dentro de las opciones ')
        if option_5=='1':
         self.register_shipment()

        elif option_5=='2':
          self.search_shipment_customer()

        else:
          break
       
      elif option=='6':
        options_6=['Generar Informes de Ventas','Generar Informes de Pagos','Generar Informes de Envios','Salir']
        for index_ops_6 in range(len(options_6)):
          print(f'''{index_ops_6+1}.{options_6[index_ops_6]}''')
        option_6=input('Ingrese la opción deseada: ')
        while not option_6.isnumeric() or not int(option_6)-1 in range(len(options_6)):
          option_6=input('Error! Ingrese un numero dentro de las opciones ')
        if option_6=='1':
         pass

        elif option_6=='2':
          pass

        elif option_6=='3':
          pass

        else:
          break
       
      else:
        break
        