def convertir(tipo_pesos, valor_dolar):                             # Funcion que guarda dos parametros 
    pesos = input("cuantos pesos" + tipo_pesos + " tienes?: ")         # tipo_pesos reempalza los valores del peso
    pesos = float(pesos)                                   
    valor_dolar = 3875                                      
    dolares = pesos / valor_dolar                         
    dolares = round(dolares, 2)                            
    dolares = str(dolares)                               
    print("Tienes $" + dolares + "  " + "dolares")  

    menu = """                                   
    Bienvenido al conversor de monedas 💲💰    

    1- Pesos Colombianos
    2- Pesos Argentinos
    3- Pesos Mexicanos

    Elige una opcion: """                                     #menu: Variable que guarde la informacion de opcion

    opcion = int(input(menu))                                 #opcion: almacena la informacion del mmenu en el input , 
                                                              #        segun la informacion que  escriba el usuario                                                                                                                        
    if opcion == 1:
        convertir("colombianos", 3785)                         # Se ejecuta la funcion convertir que se definio arriba
    elif opcion == 2:
        convertir("argentinos", 65)
    elif opcion == 3:
        convertir("mexicanos", 20)
    else:
        print('Ingresa una opcion correcta por favor')
    

