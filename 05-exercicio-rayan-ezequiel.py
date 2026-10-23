import os
import time
os.system('cls')

# Usar um laço for com range(1, 11)

# Formato de cada linha: 5 x 1 = 5 … 5 x 10 = 50

# Bônus: exibir uma linha por segundo com time.sleep(1)
numero = float(input('Digite um número: '))
for i in range(1, 11):
    time.sleep(1)
    print(f'{numero} x {i} = {numero * i}')
    
    