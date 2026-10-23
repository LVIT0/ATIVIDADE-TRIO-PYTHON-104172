import os
import time
os.system('cls')


print('Finaceiro Confia')

while True:
    
    renda_mensal_cliente = float(input('Digite sua Renda Mensal: '))
    valor_emprestimo = float(input('Digite o Valor do Empréstimo: '))
    numero_de_prestacoes = int(input('Digite o número de prestações: '))
    
    # O empréstimo pode ser de no máximo 10x a renda mensal
    # A prestação pode ser de no máximo 30% da renda mensal
    # Mostrar o valor da prestação e se o crédito foi aprovado ou negado
    
    if valor_emprestimo > (renda_mensal_cliente * 10):
        print('Credito Reprovado.')
        print('O valor do emprestimo é muito alto para sua renda.')
        time.sleep(3)
        continue
        
    else:
        prestacao_maxima = renda_mensal_cliente - (renda_mensal_cliente * 0.30)
        valor_prestacao = valor_emprestimo / numero_de_prestacoes
        
        if valor_prestacao > prestacao_maxima:
            print('Credito Reprovado.')
            print('O valor da prestação, é maior que 30%.')
            continue
        else:
            print('Credito Aprovado.')
            print(f'O valor da prestação: {valor_prestacao}.')
    
    saida = input('Deseja sair ? S para Sim e N para Não.').lower()
    if saida == 'S':
        break
    else:
        continue