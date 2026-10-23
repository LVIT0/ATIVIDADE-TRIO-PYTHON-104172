import os
os.system('cls')

# A Mundo Eletro precisa do módulo de pagamento do seu caixa. O programa lê o valor do produto e a forma de pagamento:
# 1 para à vista, 2 para a prazo.

# CRITÉRIOS DE ACEITE

# À vista: 10% de desconto sobre o valor do produto

# A prazo: pedir a quantidade de parcelas, no máximo 6, sem desconto

# Mostrar valor, forma de pagamento, desconto ou parcelas, valor da parcela e total


print('Mundo Eletro')
while True:
    valor_do_produto = float(input(' Valor do produto: '))

    print(f'1 - À vista: 10% de desconto sobre o valor do produto')
    print('2 - À prazo: pedir a quantidade de parcelas, no máximo 6, sem desconto')
    
    escolha = input('Escolha: ')
    
    if escolha == '1':
        valor_com_desconto = valor_do_produto - (valor_do_produto * 0.10)
        print(f'Valor final: {valor_com_desconto}.')
        break
    elif escolha == '2':
        parcela = int(input('Quantas parcela você deseja no máximo 6: '))
        if parcela > 6:
            print('quantidade de parcela, ultrapassa o permitido.')
            continue
        else:
            valor_parcela = valor_do_produto / parcela
            print(f'Valor final: {valor_parcela}.')
            break
    else:
        print('Opção inválida.')
        continue