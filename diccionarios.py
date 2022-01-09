def run():

    # mi_diccionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3
    # }
    

    # print (mi_diccionario['llave1'])
    # print (mi_diccionario['llave2'])
    # print (mi_diccionario['llave3'])


    Jugadores = {
        'Colombia': 'Falcao , James , Cuadrado , Ospina ',
        'Argentina': 'Messi , Dybala , Dimaria , Icardi ',
        'Brasil': 'Neymar , Dani Alves , Marquinos , Richarlison'
    }
    
    for pais in Jugadores.values():
        print(pais)

    for pais in Jugadores.keys():
        print(pais)

    for pais , jugador in Jugadores.items():
        print(pais + ' ' + 'tiene estos jugadores: ' + ' ' + jugador)

if __name__ == '__main__':
       run()