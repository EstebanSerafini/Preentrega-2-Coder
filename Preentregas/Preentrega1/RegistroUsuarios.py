usuario = str
clave = str
registro = dict()

#Funcion registro
def nuevo_usuario(id, pasw):
  '''Funcion para registrar un nuevo usuario'''
  return registro.update({usuario:clave}) 

  #Funcion Lectura
def leer_registro():
  '''Funcion para leer el diccionario de registros'''
  for x in registro.items():
    key = x[0]
    value = x[1]
    print(f'Usuario Registrado: {key} y su contraseña es: {value}')

    #Funcion para el Login
def login():
  '''Funcion para Loguear'''
  print('Login sensible a minusculas y mayusculas')
  user = input('ingrese nombre de usuario ')
  pasw = input('ingrese la contraseña ')

  for x, y in registro.items():
    if user == x and pasw == y:
      print(f'Bienvenido {x} Iniciaste Sesion Correctamente')
      break
  else:
    print('Usuario o contraseña incorrecto')

    print('Bienvenido, que desea hacer?')

while True:
  print('''Menu:
  Opcion 1 = Registrar Usuario
  Opcion 2 = Lectura de Usuarios y Claves Registradas
  Opcion 3 = Login
  Opcion 4 = Finalizar
  ''')
  opcion = input('Ingrese la opcion deseada ')
  if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
    print('opcion incorrecta')
    continue
  elif opcion == '1':
    usuario = input('Ingrese el nombre de usuario a registrar ')
    clave = input('Ingrese la clave ')
    nuevo_usuario(usuario, clave)
    print(f'Registraste el usuario {usuario} y la contraseña {clave} correctamente')
    continue
  elif opcion == '2':
    leer_registro()
    continue
  elif opcion == '3':
    login()
    break
  elif opcion == '4':
    print('Saludos, el programa finalizó')
    break
