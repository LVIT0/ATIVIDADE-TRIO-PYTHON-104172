import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

print('Prefeitura de Vila Nova')

salarios = []
familias = 0
filhos = 0

while True:
    print("╔════════════════════════════════════════════════╗")
    print("║           PREFEITURA DE VILA NOVA              ║")
    print("║         SISTEMA DE PESQUISA MUNICIPAL          ║")
    print("╠════════════════════════════════════════════════╣")
    print("║                                                ║")
    print("║  1 – Adicionar família                         ║")
    print("║  2 – Sair e exibir resultados                  ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")    
    escolha = int(input('Escolha: '))
    if escolha == 2 and familias == 0:
        print('Você não adicionou família.Tente novamente em 5 segundos...')
        time.sleep(5)
        continue
    elif escolha == 1:
        familias += 1
        salario = float(input('Digite o salario da familia: '))
        salarios.append(salario)
        filho = int(input('Digite a quantidade de filhos: '))
        filhos += filho
        continue
    elif escolha == 2:
        print(f'Total de famílias: {familias}.\nMédia de salário: {sum(salarios)  / familias:.2f}.\nMédia de filhos: {filhos / familias:.0f}')
        break
    else:
        print('Error.\nOpcção inválida.\nTente novamente mais tarde.')
        time.sleep(5)
        continue