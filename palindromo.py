def palindromo(palabra):            
    palabra = palabra.replace(' ', '')         # Replace elimina los espacios
    palabra = palabra.lower()                  # Pasar la palabra a minusculas
    palabra_invertida = palabra[::-1]          # Generar los caracteres de la palabra de manera invertida desde el 1
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
