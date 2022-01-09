#def run():

#   ============  EJEMPLO 1 =============  #


#     for contador in range(1000):
#         if contador % 2 != 0:
#             continue
#         print(contador)


#   ============  EJEMPLO 2 =============  #


#     for i in range(10000):
#         print(i)
#         if i == 5678:
#            break


#   ============  EJEMPLO 3 =============  #


    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)


    # if __name__ == '__main__':
    #        run()

#while continue 

def run():

    i = 0
    while i<10:
        i+=1
        if i==7 or i==8:
            continue
        print(i)


if __name__ == '__main__':
       run()

#while break

def correr():

    i = 0
    while i<100:
        i+=1
        if i==50 or i==55:
            break
        print(i)


if __name__ == '__main__':
       correr()
