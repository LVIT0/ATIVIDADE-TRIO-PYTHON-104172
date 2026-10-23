import os
import time
os.system('cls')


while True:
    renda_mensal = float(input('Dgitie a sua renda mensal: '))
    valor_emprestimo = float(input('Digite o valor do empréstimo: '))
    numero_de_prestacoes = int(input('Digite o número de prestações: '))

    if valor_emprestimo > (renda_mensal * 10):
        print('O valor de empréstimo é muito alto para sua renda mensal')
        time.sleep(3)
        continue
    else:
        prestacao_maxima = renda_mensal - (renda_mensal * 0.30)
        valor_prestacao = valor_emprestimo / numero_de_prestacoes

        if valor_prestacao > prestacao_maxima:
            print('Crédito Reprovado.')
            print('O valor da prestação é maior que 30%. ')
            continue
        else:
            print('Crédito Aprovado.')
            print(f'O valor da prestação: {valor_prestacao}')
    pergunta = input('Se deseja continuar, aperte "S", se não, aperte "N": ').upper()
    if pergunta == 'S':
        continue
    else:
        print('Encerrado!')
        break