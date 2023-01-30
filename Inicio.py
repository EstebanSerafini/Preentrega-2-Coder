from Preentregas.Preentrega2.Cliente import Cliente

print('Bienvenido al supermercado, para comprar debe proporcionar sus datos')

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
telefono = input('Ingrese su telefono: ')
direccion = input('Ingrese su direccion: ')

cliente = Cliente(nombre, edad, telefono, direccion)

print(f'Bienvenido {cliente.nombre}, tenemos de todo, puede comprar lo que se le ocurra.')

y = True
while y == True:
    producto = input(f'Que desea comprar? ')
    cliente.comprar(producto)
    a = input(f'Desea agregar mas productos al carrito? responda: si o no: ')
    if a == "si":
        pass
    elif a == "no":
        y = False
        break
    elif a != "si" and a != "no":
        print(f'Opcion incorrecta, vuelva cuando se decida {cliente.nombre}')

print(f'Perfecto {cliente.nombre}, Compraste {cliente.lista_compras}, gracias vuelva pronto')