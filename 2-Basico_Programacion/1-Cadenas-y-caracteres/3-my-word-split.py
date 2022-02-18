#! 2-my-split.py
#
# En códigos anteriores vimos que hay unas funciones que aplican sobre cadenas
# que se escriben con la sintexis
#       <cadena>.<funcion>(<argumentos>)
# auqnue esto es muy útil, es bueno entender cómo funciona el algoritmo
# para realizar procesos

# Escribiremos una versión propioa de la función que cambia todas
# las letras a mayúsculas, sacando privecho del Unicode
#

string = input("Dame una cadena:")

# Delimitadores de palabras
blank = ' '
nline = '\n'
tab = '\t'
comma = ' '

my_string = ''         # Creemos una cadena vacía que llenaremos poco a poco
my_list = []            # Creemos una lista vacía donde guardaremos nuestras palabras

inside_word = True      # Definamos una varible que me diga si estoy en una palabra
outside_word = False    # y una si estamos fuera
status = outside_word    # Y una de status, y supongamos que no estamos en una palabra

i = 0                   # i es el numero con el que iremos recorriendo los elementos de string
print(string[i])
while i < len(string)-1:
    s = string[i]
    if(s != blank and s != nline and s != tab and s != comma):
        status = inside_word
    while status == inside_word:
        if(s != blank and s != nline and s != tab and s != comma):
            my_string += s
        else:
            status = outside_word
            print(my_string)
            my_list.append(my_string)
            my_string  = ''
    s = string[i]
    i += 1
