
#==========================================================================================================#


# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones!')


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


#==========================================================================================================#


# opcion = int(input('Elige una opcion (1, 2, 3):'))
# if opcion == 1:
#     print('Hola')
#     print('Como estas')
#     print('Elegiste la opcion 1')
#     print('Adios')
# elif opcion == 2:
#     print('Hola')
#     print('Como estas')
#     print('Elegiste la opcion 2')
#     print('Adios')
# elif opcion == 3:
#     print('Hola')
#     print('Como estas')
#     print('Elegiste la opcion 3')
#     print('Adios')
# else:
#     print('Escribe la opcion correcta')
 
     
#==========================================================================================================#

# def x(error):
#     print(error)

# def impresion(mensaje):
#     print('Hola')
#     print('Como estas')
#     print(mensaje)
#     print('Adios')

# opcion = int(input('Elige una opcion (1, 2, 3):'))
# if opcion == 1:
#     impresion('Elegiste la opcion 1')
# elif opcion == 2:
#     impresion('Elegiste la opcion 2')
# elif opcion == 3:
#     impresion('Elegiste la opcion 3')
# else:
#     x('Escribe una opcion correcta')     


import random

Desayuno = ('Tamal', 'Huevos y pan', 'Changua')
def selectRandom(comida):
  return random.choice(Desayuno)  

Almuerzo = ('Bandeja paisa', 'Arroz con pollo', 'Ajiaco')
def selectRandom(Almuerzo):
  return random.choice(Almuerzo) 

Cena = ('Hamburguesa', 'Perro Caliente', 'Pizza')
def selectRandom(Cena):
  return random.choice(Cena) 

def run():
 
 while True: 
     opcion = (input( """Elige el tipo de comida: 
 
     1. Desayuno
     2. Almuerzo
     3. Cena 
      """))
 
     if  opcion  == "1":

         print('Haz seleccionado deayuno, El menu del día es: ', selectRandom(Desayuno) )
         break

     elif  opcion  == "2":

         print('Haz seleccionado deayuno, El menu del día es: ', selectRandom(Almuerzo) )
         break 
     elif  opcion  == "3":
       
         print('Haz seleccionado deayuno, El menu del día es: ', selectRandom(Cena) )
         break 

     elif opcion != (0, 3):
         print ('Selecciona de nuevo')
         continue

    

if __name__ == '__main__':
    run()  
