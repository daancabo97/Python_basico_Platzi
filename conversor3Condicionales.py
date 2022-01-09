menu = """                                   
Bienvenido al conversor de monedas 💲💰    

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opcion: """                                     #menu: Variable que guarde la informacion de opcion

opcion = int(input(menu))                                 #opcion: almacena la informacion del mmenu en el input , 
                                                          #        segun la informacion que  escriba el usuario
                                                                
if opcion == 1:
    pesos = input("cuantos pesos Colombianos tienes?: ")      
    pesos = float(pesos)                                   
    valor_dolar = 3875                                      
    dolares = pesos / valor_dolar                         
    dolares = round(dolares, 2)                            
    dolares = str(dolares)                               
    print("Tienes $" + dolares + "  " + "dolares")  
elif opcion == 2:
    pesos = input("cuantos pesos Argentinos tienes?: ")      
    pesos = float(pesos)                                   
    valor_dolar = 102.60                                 
    dolares = pesos / valor_dolar                         
    dolares = round(dolares, 2)                            
    dolares = str(dolares)                               
    print("Tienes $" + dolares + "  " + "dolares")  
elif opcion == 3:
    pesos = input("cuantos pesos Mexicanos tienes?: ")      
    pesos = float(pesos)                                   
    valor_dolar = 20.68                                   
    dolares = pesos / valor_dolar                         
    dolares = round(dolares, 2)                            
    dolares = str(dolares)                               
    print("Tienes $" + dolares + "  " + "dolares")  
else:
    print('Ingresa una opcion correcta por favor')
    

