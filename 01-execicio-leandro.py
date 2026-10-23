import os
os.system('cls')


while True:
    numero_1 = float(input('Digite o primeiro número: '))
    operador = input('Digite  o operador: ')
    numero_2 = float(input('Digite o segundo número: '))

    match operador:
        case '+':
            print(f'a adição é: {numero_1 + numero_2} ')
        case '-':
            print(f'a subtração é: {numero_1 - numero_2} ')
        case '/':
            if numero_2 > 0:
                print(f'a divisão é: {numero_1 / numero_2} ')
            else:
                print('Não pode dividir por zero.')
        case '*':
            print(f'a multiplicação é: {numero_1 * numero_2}')

    pergunta = input('Deseja continuar? "S" ou "N": ').upper()
    if pergunta == 'S':
        continue
    else:
        print('Encerrado!')
        break