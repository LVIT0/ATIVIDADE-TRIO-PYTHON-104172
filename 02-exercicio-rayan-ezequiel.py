import os
os.system('cls')

# Desconto por quantidade no caixa
# O caixa do Atacarejo Bom Preço precisa calcular descontos automaticamente.
# O programa lê o nome do produto, a quantidade comprada e o preço unitário.
# CRITÉRIOS DE ACEITE
# Total = quantidade x preço unitário
# Até 5 unidades: 2% · de 6 a 10: 3% · acima de 10: 5%
# Mostrar o produto, o total, o desconto e o total a pagar

print('Atacarejo Bom Preço')

while True:
    
    nome_do_produto = input('Digite o nome do produto: ')
    quantidade_comprada = int(input('Qual foi a quantidade: '))
    preco_unitario = float(input('Digite o preço unitario: '))

    total = quantidade_comprada * preco_unitario
    
    if quantidade_comprada <= 5:
        total_a_pagar = total - (total * 0.02)
        print(f'Produto: {nome_do_produto}\nTotal: {total}\nDesconto: {preco_unitario * 0.02}%\nValor final: {total_a_pagar}')
        break
    elif quantidade_comprada >= 6 and quantidade_comprada <= 10:
        total_a_pagar = total - (total * 0.03)
        print(f'Produto: {nome_do_produto}\nTotal: {total}\nDesconto: {preco_unitario * 0.03}%\nValor final: {total_a_pagar}')
        break
    elif quantidade_comprada > 10:
        total_a_pagar = total - (total * 0.05)
        print(f'Produto: {nome_do_produto}\nTotal: {total}\nDesconto: {preco_unitario * 0.05}%\nValor final: {total_a_pagar}')
        break
    
    saida = input('Deseja sair ? S para Sim e N para Não.').lower()
    if saida == 'S':
        break
    else:
        continue