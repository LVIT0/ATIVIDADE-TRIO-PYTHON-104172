import os
os.system('clear')


notas = []

while True:
    nota = float(input('Digite sua nota: '))
    
    if nota < 0 or nota > 10:
        print('Nota inválida. tente novamente.')
        continue

    else:
        notas.append(nota)
        if len(notas) == 3:
            media = sum(notas) / len(notas)
            if media >= 7:
                print(f'Sua média foi: {media}, Você está aprovado.')
                break
                
            elif media >= 5 or media >= 6.9: 
                print(f'Sua média foi: {media}, Você está em recuperação.')
                break
            
            else:
                print(f'Sua média foi: {media}, Você está em reprovado.')
                break
