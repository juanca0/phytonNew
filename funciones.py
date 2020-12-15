# def imprimir_mensaje():
#     print('mensaje especial: ')
#     print ('!Estoy aprendiendo funciones')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(option):
    print ('Hola')
    print('Como estás')
    print(f'Elegiste la opción {option}')
    print('Adios')

option = int(input('Elige una opcion(1, 2, 3): '))
if option == 1:
    conversacion(option)
elif option == 2:
    conversacion(option)
elif option == 3: 
   conversacion(option)
else:
    print('Escribe la opcion correcta ')