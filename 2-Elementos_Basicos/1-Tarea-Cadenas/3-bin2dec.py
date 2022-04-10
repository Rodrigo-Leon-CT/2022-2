base = input('Ingresar número en base binario: ') 
string_binarios = str(base)
posicion = 0 
decimal = 0 

base = base[::-1] 
# El valor de la variable es el valor del número ingresado,solo que leído de derecha a izquierda.

for digito in base: 
#Para cada dígito se realiza la operacion de la siguienre linea 
    operacion = 2**posicion 
    decimal = decimal + int(digito) * operacion 
# El valor final será el valor de las operaciones realizadas             
    posicion += 1 
    
string_decimal = str(decimal)
print(f'Número base binaria: ' + string_binarios + ', Número base decimal: ' + string_decimal)
