import os
os.system('cls')
import time
# Calculadora para os atendentes

# Os atendentes da CrediFácil precisam de uma calculadora rápida no terminal.
# Desenvolvam um programa que peça dois números e um operador (+, -, * ou /) e use match-case para escolher a operação.
# CRITÉRIOS DE ACEITE
# Mostrar os dois números, o operador escolhido e o resultado
# Operador inválido cai no case _ com uma mensagem de aviso
# Bônus: impedir a divisão por zero

while True:
    print('OPERAÇÕES')
    numero_um = float(input('Digite o primeiro número: '))
    operador = input('Digite o Operador: ')
    numero_dois = float(input('Digite o segundo número: '))

    match operador:
        case '+':
            print(f'A soma é: {numero_um + numero_dois}')
        case '-':
            print(f'A subtração é: {numero_um - numero_dois}')
        case '/':
            if numero_dois == 0:
                print('Não é divisivel por 0.')
                time.sleep(5)
                os.system('cls')
                continue
            print(f'A divisão é: {numero_um / numero_dois}')
        case '*':
            print(f'A multiplicação é: {numero_um * numero_dois}')
        case _:
            print('Error: Operador Inválido.')
    saida = input('Deseja continuar ? S para Sim e N para Não. ').upper()
    if saida == 'N':
        break
    