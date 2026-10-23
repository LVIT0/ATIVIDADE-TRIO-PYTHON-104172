import os 
os.system('cls')

while True:
    produto = str(input("Digite o nome do produto: "))
    quantidade = int(input("Digite a quantidade comprada: "))
    preco = float(input("Digite o valor do produto:"))
    
    total = preco * quantidade
    
    if quantidade <= 5:
        desconto = total * 0.02
    elif 6 <= quantidade <= 10:
        desconto = total * 0.03
    elif quantidade > 10:
        desconto = total * 0.05
    
    
    preco_com_desconto = total - desconto
    
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Desconto: {desconto}")
    print(f"Preço com desconto: {preco_com_desconto:2f}")