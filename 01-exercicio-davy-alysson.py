import os
os.system("cls")

while True:
    
    num_1 = float(input("Digite o primeiro número:"))
    
    print("OPERAÇÕES")
    print("+ -> SOMA")
    print("- -> SUBTRAÇÃO")
    print("x -> MULTIPLICAÇÃO")
    print("/ -> DIVISÃO")
    
    operacao = input("Qual operação desejas?")
    num_2 = float(input("Digite o segundo número:"))
    
    match operacao:
        case '+':
            os.system("cls")
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
        case '-':
            os.system("cls")
            print(f"{num_1}  - {num_2} = {num_1 - num_2}")
        case 'x':
            os.system("cls")
            print(f"{num_1} x {num_2} = {num_1 * num_2}")
        case '/':
            if num_2 == 0:
                os.system("cls")
                print("Não divisivel por 0")
                continue
            else:
                os.system("cls")
                print(f"{num_1} / {num_2} = {num_1 / num_2}")
        case _:
            print("SEM A OPERAÇÃO SELECIONADA")
            os.system("cls")
    escolha = input("Deseja recomeçar? S para SIM e N para NÃO: ").upper()
    
    match escolha:
        case "N":
            break
        case "S":
            os.system("cls")
            continue