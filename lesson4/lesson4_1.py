# list список
products = ['cheess','ketchup', 'bread', 'water']
print(len(products))
print(products[-1], products[0])
print(products[0:3])
print(products[1:])
print(products[:2])
print(products[::-1])
print(products[0:4:2])
products[0] = 'juice'
products[0:3] = 'juice', 'K', 'H'
print(products)

