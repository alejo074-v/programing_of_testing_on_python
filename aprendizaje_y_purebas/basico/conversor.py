def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')
    
def conversor(tipo_de_pesos, valor_dolar):    
    pesos = float(input("¿Cúantos pesos " + tipo_de_pesos + " tienes?: "))
    valor_dolar = valor_dolar
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenidos al conversor de monedas 💰

1 - Pesos  colombianos
2 - Pesos argentinos
3 - pesos mexicanos

Elige una opción:: """

opcion = int(input(menu))

if opcion ==1:
    conversacion('Elegiste la opción 1')
elif opcion ==2:
el    conversacion('Elegiste la opción 2')
elif opcion ==3:
el    conversacion('Elegiste la opción 3')
else:
    conversacion('Elige una opción correcta')

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentina", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("Ingresa una opcion valida por favor 😊\n")
