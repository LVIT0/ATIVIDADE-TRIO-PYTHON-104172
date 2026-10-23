import os
os.system('cls')


while True:
    valor_produto = float(input('Digite o valor do produto: '))
    forma_pagamento = input('Qual a forma de pagamento? Digite 1 para à vista ou 2 para a prazo: ')

    if forma_pagamento == 1:
        valor_desconto = valor_produto - (valor_produto * 0.10)
    elif forma_pagamento == 2:
        pergunta = int(input('Quantas parcelas voçê deseja: '))