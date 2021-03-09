def run():
    # motrar solo pares
    # for cont in range(100):
    # if cont % 2 == 0:
    #     print(f"{cont} es par")
    # else:
    #     print(f"{cont} es impar")
    # if cont % 2 != 0:
    #     continue
    # print(cont)

    # utilizar break para cuando llegue
    # for i in range(100):
    #     print(i)
    #     if i == 55:
    #         break

    # text = input("Escribe un texto: ")
    # for letra in text:
    #     if letra == "o":
    #         break
    #     print(letra)

    # imprimir pares con while
    # LIMITE = 100
    # i = 0
    # while i < LIMITE:
    #     if i % 2 != 0:
    #         i += 1
    #         continue
    #     print(i)
    #     i += 1

    # utilizar break en while
    LIMITE = 100
    i = 0
    while i < LIMITE:
        if i == 40:
            break
        print(i)
        i += 1


if __name__ == "__main__":
    run()