from Store import Store
import requests
Inventory = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json') 
Old_inventory=Inventory.json()
new_products = []
new_customers = []
sales = []
pagos = []
orders = []
shipments = []

def main():
  store = Store(Old_inventory, new_products, new_customers, sales, pagos, orders, shipments)
  store.initial_products()
  # # store.ShowSt()
  store.menu()
  
main()