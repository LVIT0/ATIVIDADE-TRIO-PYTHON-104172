import os
os.system('cls')


nota1 = float(input("Digite a 1ª nota (entre 0 e 10): "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida O valor deve estar entre 0 e 10")
    nota1 = float(input("Digite a 1ª nota novamente: "))


nota2 = float(input("Digite a 2ª nota (entre 0 e 10): "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida O valor deve estar entre 0 e 10")
    nota2 = float(input("Digite a 2ª nota novamente: "))


nota3 = float(input("Digite a 3ª nota (entre 0 e 10): "))
while nota3 < 0 or nota3 > 10:
    print("Nota inválida O valor deve estar entre 0 e 10")
    nota3 = float(input("Digite a 3ª nota novamente: "))


media = (nota1 + nota2 + nota3) / 3

print(f"Média final: {media:.2f}")


if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
