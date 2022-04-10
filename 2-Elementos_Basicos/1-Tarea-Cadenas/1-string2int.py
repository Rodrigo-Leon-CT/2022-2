
numero_principal = input('Ingresar un número entero decimal: ') 

numero_principal = str (float(numero_principal))
    
numero_entero, numero_decimal = numero.split('.') 
# Se hace un split con punto para separar lo el mumero entero del decimal y asignamos
                                     #las variables num_ent y num_dec.
    
numero_entero = float(numero_principal)
 #La cadena se converte en número flotante.

entero = round(numero_entero) 
# Al numero se va a redonderar a partir de .6

print(f'{entero} ,' , type(entero)) 


