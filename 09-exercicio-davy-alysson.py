import os
os.system("cls")

valor = 0
quantidade = 0

while True:
    print("==================================================")
    print("             CARDÁPIO DO RESTAURANTE              ")
    print("==================================================")
    print("Cód. | Prato                        |      Preço")
    print("--------------------------------------------------")
    print(" 01  | X-Burger Especial            |     R$ 35.50")
    print(" 02  | Pizza Margherita             |     R$ 45.00")
    print(" 03  | Lasanha à Bolonhesa          |     R$ 42.00")
    print(" 04  | Salada Caesar                |     R$ 28.50")
    print(" 05  | Filé de Frango Grelhado      |     R$ 32.00")
    print("==================================================")

    escolha = input("Escolha: ")


        
    match escolha:
        case "1":
            valor += 35.50
            quantidade += 1
        case "2":
            valor += 45.00
            quantidade += 1
        case "3":
            valor += 42.00
            quantidade += 1
        case "4":
            valor += 28.50
            quantidade += 1
        case "5":
            valor += 32.00
            quantidade += 1
        case _:
            print("Sem opção disponivel")
            continue
    
    continua = input("Deseja continuar? ").upper()
    
    if continua == "N":
        break
    elif continua == "S":
        continue

print(f"Valor total: {valor}")
print(f"Quantidade de pratos: {quantidade}")