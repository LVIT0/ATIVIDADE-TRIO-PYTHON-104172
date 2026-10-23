import os
os.system("cls")

while True:
    renda_mensal = float(input("Digite a sua renda mensal: "))
    emprestimo_pedido = float(input("Digite quanto você deseja: "))
    num_prestacoes = int(input("Quantas prestações de seja? "))
    valor_prestacao = emprestimo_pedido / num_prestacoes
    
    if renda_mensal * 10 >= emprestimo_pedido and renda_mensal * 0.3 >= valor_prestacao:
        print(f"Sua renda é R${renda_mensal}")
        print(f"O emprestimo desejado foi de R${emprestimo_pedido}")
        print(f"Em {num_prestacoes}x cada uma de R${valor_prestacao:.2f}")
        print(f"O crédito foi aceito")
    else:
        print(f"Sua renda é R${renda_mensal}")
        print(f"O emprestimo desejado foi de R${emprestimo_pedido}")
        print(f"Em {num_prestacoes}x cada uma de R${valor_prestacao:.2f}")
        print(f"O crédito foi negado")
        
        