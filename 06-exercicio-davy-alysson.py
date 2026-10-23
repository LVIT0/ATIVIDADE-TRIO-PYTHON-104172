import os
os.system('cls')
soma = 0
numeros_pares = 0
numeros_impares = 0

for i in range (1, 6):
    numero = int(input(f"Digite o {i}° número: "))
    soma += numero
    
       
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
        
print(f"NUMEROS PARES: {numeros_pares}")
print(f"NUMEROS IMPARES: {numeros_impares}")
print(f"SOMA = {soma}")
        