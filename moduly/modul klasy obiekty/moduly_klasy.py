class Product:
    pass
class Apple:
    pass
class Potatoe:
    pass
class Order:
    pass

if __name__ == "__main__":
    ligol = Apple()
    pulowia = Apple()

    mlode_ziemniaki = Potatoe()
    stare_ziemniaki = Potatoe()

    print('Ligol',type(ligol))
    print('pulowia',type(pulowia))

    print('mlode ziemniaki',type(mlode_ziemniaki))
    print('stare ziemniaki', type(stare_ziemniaki))
    orders = []
    for x in range(5):
        orders.append(Order())

    print(orders)

    produkty = {
        "jabłko": Product(),
        "gruszka": Product(),
        "pomarancza": Product()

    }
    print(produkty)