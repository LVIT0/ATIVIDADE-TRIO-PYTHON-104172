import os
os.system('clear')

print('Instituto Dados')

ambos = []
numeros_pares = []
numeros_impares = []

for i in range(5):
    numero = float(input('Digite um número: '))
    ambos.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    
print(f'Quantidade de pares: {len(numeros_pares)}')
print(f'Quantidade de impares: {len(numeros_impares)}')
print(f'Soma: {sum(ambos)}')