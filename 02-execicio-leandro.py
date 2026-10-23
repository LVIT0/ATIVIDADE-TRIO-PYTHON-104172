import os
os.system('cls')


while True:
    nome_produto = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))
    preco_unitario = int(input('Digite o preço do produto: '))
    valor_total = preco_unitario * quantidade

    if quantidade <= 5:
        valor_com_desconto = valor_total - (valor_total * 0.2)
        print('Voçê recebeu um desconto de 2%')
        print(f'O valor com desconto é: R$ {valor_com_desconto}')
    elif quantidade <= 10:
        valor_com_desconto = valor_total - (valor_total * 0.3)
        print('Voçê recebeu um desconto de 3%')
        print(f'O valor com desconto é: R$ {valor_com_desconto}')
    elif quantidade > 10:
        valor_com_desconto = valor_total - (valor_total * 0.5)
        print('Voçê recebeu um desconto de 5%')
        print(f'O valor com desconto é: R$ {valor_com_desconto}')
    pergunta = input('/nSe deseja continuar, aperte "S", se não, aperte "N": ').upper()
    if pergunta == 'S':
        continue
    else:
        break