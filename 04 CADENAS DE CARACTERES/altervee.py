"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas

"""
text_1 = "Hi"
text_2 = "Good morning"
#concat 
print(text_1+" "+text_2)

#repeticion
print(text_1*3)

#indexar
print(text_1[0])

#slice
print(text_2[2:-1])
print(text_2[:2])

#busqueda
print("o" in text_2)

#busqueda empiezan y acaban 
print(text_2.startswith("Good"))
print(text_2.endswith("ing"))

#conteo busqueda 
print(text_2.count("m"))
#encontrar la psición
print(text_1.find("Hi"))

#reemplazar

print(text_2.replace("o", "A"))

#division 
print(text_2.split("o"))

#Mayus minus
print(text_1.upper())
print(text_1.lower())
print(text_2.title())
print(text_2.capitalize())

#eliminar espacios
print("  dddd  ".strip())


#formato
print("corto:{}, largo:{}".format(text_1, text_2))

print(f"corto:{text_1}, largo:{text_2}")

#lista
print(list(text_1))

#comprobar
print(text_1.isalpha())
print(text_1.isnumeric())
print(text_1.isalnum())


#extra
#palindromo
def is_palindromo(f1:str):
    if f1==f1[::-1]:# dar la vuelta
        print("Si es un palindromo")
    else:
        print("No es un palindromo")
is_palindromo("ete")

#anagrama
def is_anagrama(f1:str, f2:str):
    if sorted(f1)==sorted(f2):
        print("Si es un anagrama")
    else:
        print("No es un anagrama")
is_anagrama("roma", "amor")

#anagrama
def is_isograma(f1:str):
    word_dic=dict()
    for word in f1:
        word_dic[word] = word_dic.get(word, 0) + 1
    
    isogram=True
    iso_values = list(word_dic.values())
    iso_len = iso_values[0]
    for word in iso_values:
        if word != iso_len:
            isogram = False
            print("No es un isograma")
    if isogram is not False:
        print("es un isograma")

is_isograma("romm")