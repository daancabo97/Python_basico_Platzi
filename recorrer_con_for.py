#=============================================================== Ejemplo 1 : ==================================================================


# def run():
#     nombre = input('Escribe tu nombre: ')
#     for letra in nombre:                  #   => para las letras en el nombre vamos a imprimir cada una de las letras en cada vuelta del ciclo
#         print(letra)

# if __name__ == '__main__':
#     run()


#=============================================================== Ejemplo 2 : ==================================================================


def run():
     frase = input('Escribe una frase')
     for caracter in frase:
        print(caracter.upper())             #   => para los caracteres en la frase vamos a imprimir cada uno de los caracteres en MAYUSCULA en cada vuelta del ciclo

if __name__ == '__main__':
    run()

