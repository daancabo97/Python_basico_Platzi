#==========================================================    EJEMPLO 1 :   ===================================================================
# import random


# def run():
#     numero_aleatorio = random.randint(1, 100)
#     numero_elegido = int(input('Elige un numero del 1 al 100: '))
#     while numero_elegido != numero_aleatorio:
#         if numero_elegido < numero_aleatorio:
#             print('busca un numero mas grande')
#         else:
#             print('Busca un numero mas pequeño')
#         numero_elegido = int(input('Elige otro numero: '))
#     print('¡Ganaste!')


# if __name__ == '__main__':
#     run()


#==========================================================    EJEMPLO 2 :   ===================================================================
import random
import sys



def run():
    num_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número entre 1 y 100: '))
    vidas = 10
    while numero_elegido != num_aleatorio:
        if vidas == 0:
            print('Perdiste, más suerte para la próxima.')
            sys.exit(0)
            break
        if numero_elegido < num_aleatorio:
            print ('Busca un número más grande, te quedan ' + str(vidas) +  ' vidas')
            vidas -= 1
        elif numero_elegido > num_aleatorio:
             print ('Busca un número más chico, te quedan ' + str(vidas) + ' vidas')
             vidas -= 1
        numero_elegido = int(input('Elige un número entre 1 y 100: '))       
    print ('¡Felicidades, ganaste!')


if __name__ == '__main__':
    run()