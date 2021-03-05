def run():
    palabra = input("ingresa palabra ")
    for letra in palabra:
        if letra == letra.lower():
            print(f"{letra} es minuscula")
        else:
            if letra == letra.upper():
                print(f"{letra} es mayuscula")
            else:
                print("no es nada ")


if __name__ == "__main__":
    run()