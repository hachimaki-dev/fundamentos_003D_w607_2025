import random
vidas = 3
dif1 = 0
dif2 = 0

print("Bienvenido al juego en donde debes adivinar mi numero\nA continuacion, ingresa 2 numeros diferentes")
num1 = int(input("Limite menor: "))
num2 = int(input("Limite mayor: "))
if num1 > num2:
    print("ERROR, el primer numero debe ser menor que el segundo :(")

from random import randint
numero = randint(num1, num2)


if vidas == 3:
    intento1 = int(input("Este es tu primer intento, trata de adivinar mi numero: "))
    if intento1 == numero:
        print("WOW felicidades! adivinaste a la primera!")
    else:
        if intento1 < numero:
            print("Lo siento pero tu numero es menor al mio, sigue intentando")
        elif intento1 > numero:
            print("Lo siento pero tu  numero es mayor al mio, sigue intentando")
        vidas -= 1
else:
    print("Ha ocurrido un error, vuelve a iniciar el programa.")

if vidas == 2:
    intento2 = int(input("Este es tu segundo intento, podras adivinar mi numero?: "))
    if intento2 == numero:
        print("Felicidades! lograste adivnar a la segunda vez!")
    else:
        if intento2 > numero:
            print("Lo siento pero tu numero es mayor al mio")
        else:
            print("Uy lo siento pero tu numero es menor al mio...")
        vidas -= 1
    
    if intento1 > numero:
        dif1 = intento1 - numero
    else:
        dif1 = numero - intento1
    if intento2 > numero:
        dif2 = intento2 - numero
    else:
        dif2 = numero - intento2

    if dif2 < dif1:
        print("Tu segundo numero estuvo mas cerca que tu primer numero!")
    elif dif1 < dif2:
        print("Tu primer numero estuvo mas cerca que tu segundo numero!")
    else:
        print("Uy en este caso, tanto tu numero 1 como el numero 2 estan igual de cerca!")

if vidas == 1:
    intento3 = int(input("Este es tu tercer y ultimo intento, la tercera sera la vencida?: "))
    if intento3 == numero:
        print("Al parecer, la tercera es la vencida, felicidades, has ganado!")
    else:
        if intento3 < numero:
            print("Tu numero es menor al mio y has perdido!")
        elif intento3 > numero:
            print("Tu numero es mayor que el mio y has perdido")
    vidas = 0

if vidas == 0:
    print(f"Has perdido, de todas formas, el numero era: {numero}")