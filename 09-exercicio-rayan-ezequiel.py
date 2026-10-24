import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

print('Restaurante do Sabor')
print("\n┌────────────────────────────────────────────────────────┐")
print("│                    C A R D A P I O                     │")
print("│                      MENU PRATOS                       │")
print("├────────────────────────────────────────────────────────┤")
print("│                                                        │")
print("│ 1 - Filé Mignon ao Molho Madeira..............R$ 68.90 │")
print("│ 2 - Frango Grelhado com Ervas.................R$ 42.50 │")
print("│ 3 - Salmão Grelhado com Maracujá..............R$ 75.00 │")
print("│ 4 - Risoto de Cogumelos.......................R$ 55.00 │")
print("│ 5 - Espaguete à Carbonara.....................R$ 48.00 │")
print("│                                                        │")
print("└────────────────────────────────────────────────────────┘\n")

quantidade = 0
valor_final = 0

while True:
    prato = int(input('Escolha (pelas númerações.): '))
    match prato:
        case 1:
            print('Filé Mignon ao Molho Madeira R$ 68.90, adicionado a conta.')
            quantidade += 1
            valor_final += 68.90
        case 2:
            print('Frango Grelhado com Ervas.................R$ 42.50 foi adicionado a conta.')
            quantidade += 1
            valor_final += 42.50
        case 3:
            print('Salmão Grelhado com Maracujá..............R$ 75.00 foi adicionado a conta.')
            quantidade += 1
            valor_final += 75.00
        case 4:
            print('Risoto de Cogumelos.......................R$ 55.00 foi adicionado a conta.')
            quantidade += 1
            valor_final += 55
        case 5:
            print('Espaguete à Carbonara.....................R$ 48.00 foi adicionado a conta.')
            quantidade += 1
            valor_final += 48
    saida = input('Deseja sair ? S para sim e N para não. ')
    if saida.upper() == 'S':
        print(f'Quantidade de pratos pedidos: {quantidade}.\nValor Final: R$ {valor_final}.')
        time.sleep(5)
        break
    else:
        continue




