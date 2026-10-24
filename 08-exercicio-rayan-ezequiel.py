import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

print('Clinca Vida Plena')

# O usuário cadastra login e senha, a tela é limpa e o sistema pede os dados de novo para entrar.

# CRITÉRIOS DE ACEITE

    # Repetir o pedido enquanto login ou senha estiverem errados

    # No máximo 3 tentativas: depois disso, bloquear e encerrar

    # Acesso correto: mostrar uma mensagem de boas-vindas

print('CADASTRO.')
usuario_cadastro = input('Digite um nome de usuario: ')
senha_cadastro = input('Digite uma senha: ')

tentativas = 0
while True:
    # login
    time.sleep(3)
    print('Clinca Vida Plena')
    print('LOGIN')
    usuario_login = input('Digite seu nome de usuario: ')
    senha_login = input('Digite sua senha: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if tentativas == 3:
        print('Login foi bloqueado, tente novamente em 72 horas.')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    
    elif usuario_login != usuario_cadastro  and senha_login != senha_cadastro:
        print('Sua senha e usuario estão errados, tente novamente')
        tentativas += 1
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
        
    elif usuario_login != usuario_cadastro:
        print('Seu Usuario está errado, tente novamente')
        tentativas += 1
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    elif senha_login != senha_cadastro:
        print('Sua senha está errada, tente novamente')
        tentativas += 1
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    
    else:
        print(f'Acesso correto: Sr(a){usuario_cadastro}, seja muito bem-vindo.')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        break