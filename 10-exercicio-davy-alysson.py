import os
os.system("cls")

familias = 0
salarios = 0
filhos = 0

maior_salario = 0
menor_salario = 0

while True:
    print("1 - Adicionar família")
    print("2 - Sair e exibir resultados")

    escolha = input("Escolha: ")

    
    if escolha == "1":
        salario = float(input("Digite o salario da familia:"))
        filho = int(input("Digite quantos filhos tem na sua familia:"))
        salarios += salario
        filhos += filho
        familias += 1
        if maior_salario is 0 and menor_salario is 0:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
                    
            if salario < menor_salario:
                menor_salario = salario
    elif escolha == "2":
        print(f"Total de familias: {familias}")
        print(f"Media de salario: {salarios / familias}")
        print(f"Media de filhos: {filhos / familias}")
        print(f"Maior salario: {maior_salario}")
        print(f"Menor salario: {menor_salario}")
        break