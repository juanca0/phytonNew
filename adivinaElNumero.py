import random


def run():
    numeroRandom = random.randint(1, 100)
    numeroElegido = int(input("Elige un numero del 1 al 100: "))
    while numeroElegido != numeroRandom:
        if numeroElegido < numeroRandom:
            print("busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numeroElegido = int(input("Elige otro numero "))
    print("¡Ganaste!")


if __name__ == "__main__":
    run()