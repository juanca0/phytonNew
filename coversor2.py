def cambio_Moneda(moneda, valor_dolar, selct):
    if select == 1:
            moneda = float(moneda)
            valor_dolar = 3425.84
            dolares = moneda * valor_dolar
            dolares = round(dolares, 2)
            print(f'Los ${moneda} dolares son {dolares} en tu moneda ')
    elif select == 2:
            moneda = float(moneda)
            valor_dolar = 3425.84
            dolares = moneda / valor_dolar
            dolares = round(dolares, 2)
            print(f'En tu moneda $ {moneda} esta cantidad son ${dolares} dolares')
    else:
        print('Ingresa solo un numero de la lista ')
        


if __name__ == '__main__':
    try:
        select  = int(input('''
        Ingresa que quieres hacer:
            [1] Cambiar de dolares a tu moneda
            [2] Camabiar de tu moneda a dolares
        Selecciona: '''))
        print('*******************')
        moneda = float(input('Ingresa la cantidad que quieres convertir: '))
        valor_dolar = float(input('Ingresa el valor del dolar en tu moneda: '))
        cambio_Moneda(moneda, valor_dolar, select)
    except:
        print('*** ERROR ****')
        print('Por favor, ingresa solo valores numericos ')
