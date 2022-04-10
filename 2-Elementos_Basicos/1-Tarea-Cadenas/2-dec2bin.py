principal = int(input('Ingresar cualquier numero entero: ')) 

cadena_decimal = str(principal) 

num_binario = 0 

cont = 0 

while principal > 0: 
    
    numero  = principal % 2 
# El valor de cada dígito será el valor sera el numero valuado en 2
    
    principal = int(principal // 2) 
    
    num_binario = num_binario + numero * (10**cont) 
# El valor será la suma y multiplicación del valor por 10; esto determinará la posición del número binario
    
    cont += 1 

cadena_binaria = str(num_binario) 
 
print(' Base binaria: ' + cadena_binaria)
