menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

elige una opción """

opcion = input(menu)
if opcion == '1':
    pesos = input('Cuántos pesos Colombianos tienes: ')
    pesos = float(pesos)
    valor_dolar = 3425.84
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
elif opcion == '2':
    pesos = input('Cuántos pesos Argentions tienes: ')
    pesos = float(pesos)
    valor_dolar = 82.39
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
elif opcion == '3':
    pesos = input('Cuántos pesos Mexicanos tienes: ')
    pesos = float(pesos)
    valor_dolar = 20.20
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')
else:
    print('ingresa una opcion correcta por favor ')

