def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0

    for caracter in cadena:
        if caracter.isalpha():  
            if caracter in vocales:
                num_vocales += 1
            else:
                
                num_consonantes += 1

    print("Número de vocales:", num_vocales)
    print("Número de consonantes:", num_consonantes)
texto = input("Introduce una cadena de texto: ")
contar_vocales_consonantes(texto)
