import os
os.system('cls')

cad_login = str(input("Cadastre seu login: "))
cad_senha = int(input("Cadastre sua senha: "))
os.system('cls')

tentativas = 3

while tentativas > 0:
    login = str(input("Digite seu login: "))
    senha = str(input("Digite sua senha: "))

    if login == cad_login and senha == cad_senha:
        print("Boas vindas")
        break
    else:
        tentativas -= 1
        continue
if tentativas == 0:
    print("Numero de tentativas acabou pivete")
