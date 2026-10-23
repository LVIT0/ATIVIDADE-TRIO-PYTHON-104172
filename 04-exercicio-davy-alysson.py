import os
os.system('cls')


while True:
    valor = float(input("Digite o valor do produto:"))
    
    print("1 - À vista")
    print("2 - A prazo")
    
    escolha = input("Escolha: ")
    
    match escolha:
        case '1':
            desconto = valor * 0.1
            total_a_pagar = valor - desconto
            print(f"Valor: R${valor}")
            print(f"Forma de pagamento: 1 - À vista")
            print(f"Desconto: {desconto}")
            print(f"Valor total: {total_a_pagar}")
            break
        case '2':
            quantidade_de_parcelas = int(input("Digite quantas parcelas deseja: "))
            total_a_pagar = valor
            valor_da_parcela = total_a_pagar / quantidade_de_parcelas
            if quantidade_de_parcelas <= 6:
                print(f"Valor: R${valor}")
                print(f"Forma de pagamento: 2 - A prazo")
                print(f"Quantidade de parcelas: {quantidade_de_parcelas}")
                print(f"Valor da parcela: R${valor_da_parcela}")
                print(f"Valor total: {total_a_pagar}")
                break
            else:
                print("Pode no máximo 6 parcelas")
                continue
                
                
            
            
            
            