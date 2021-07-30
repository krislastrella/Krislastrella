products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# PROBLEM 1
def get_product(product):
    return products[product]

get_product("espresso")

# PROBLEM 2
def get_property(product,prop):
    return products[product][prop]
get_property("espresso", "price")

# PROBLEM 3
def main():
    with open("receipt.txt","w") as r:
        r.write('''
    ==
    CODE\t\tNAME\t\tQUANTITY\tSUBTOTAL''')
        orders = {}
        total = 0
        counter = {'americano': 0,
        'brewedcoffee': 0,
        'cappuccino' : 0,
        'dalgona' : 0,
        'espresso' : 0,
        'frappuccino' : 0}
        while True:
            productquantity = str(input("What's your order and quantity (product, quantity)? (Type '/' to end)"))
            if productquantity == "/":
                break
            else:
                product, quantity = productquantity.split(",")
                quantity = int(quantity)
                counter[product] += quantity
                price = counter[product] * get_property(product,"price")
                total += quantity * get_property(product,"price")
                order = products[product]["name"]
                orders.update({product:{'order':order,'price':price,'quantity':counter[product]}})

        orders = dict(sorted(orders.items()))


        for i in orders:
            r.write(f'''
        {i}\t\t{orders[i]['order']}\t{orders[i]['quantity']}\t\t{orders[i]['price']}
    ''')
        r.write(f'''
        Total:\t\t\t\t\t\t{total}
        ==
    ''')

main()
