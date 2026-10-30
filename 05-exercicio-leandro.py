import time
import os
os.system('cls')

print('TABUADA')

tabuada = int(input('\nDigite um número para tabuada: '))


for i in range(10):
    soma = tabuada * (i +1)
    time.sleep(1)
    print(f'{tabuada} X {i+1} = {soma}')