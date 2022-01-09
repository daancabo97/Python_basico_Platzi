def run():                                             #  ->  Para trabajar con un programa en python primero se define una funcion principal
     LIMITE = 100000                                   #  ->  Limite de conteo
                                                      
     contador = 0                                      #  ->  variable contador igual a 0
     potencia_2 = 2**contador                          #  ->  se define la variable potencia_2 es igual a 2 elevado a contador
     while potencia_2 < LIMITE:                        #  ->  Mientras potencia_2 sea menor al limite que imprima la potencia de 2 cierta cantidad de veces 
        print(' 2 elevado a ' + str(contador) +        #  ->  str para pasar de tipo entero a string
               ' es igual a: ' + str(potencia_2))      #  ->  str para pasar de tipo entero a string
        contador = contador + 5                        #  ->  contador es igual a contador para que cuente de a 5 en 5
        potencia_2 = 2**contador                       #  ->  se define nuevamente la potencia de 2 elevado a contador



if __name__ == '__main__':                             # -> entrypoint
     run()

