class Cliente:
    #Constructor
    def __init__(self, nombre, edad, telefono, direccion):
        
        #atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.lista_compras = []

    def __str__(self):
        return f'Bienvenido {self.nombre} ¿que desea comprar?'

    def comprar(self, producto):
        self.lista_compras.append(producto)
        return print(f'{producto} agregado al carrito.')
    