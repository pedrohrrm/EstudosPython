m1 = float(input('Digite a nota de M1: '))
m2 = float(input('Digite a nota de M2: '))
m3 = float(input('Digite a nota de M3: '))
media = (m1 + m2 + m3)/3
print(media)
if media >= 0.0 and media <= 4.0:
    print('Aluno Reprovado!')
elif media >= 4.1 and media <= 6.0:
    exame = float(input('Digite a nota do exame:'))
    if exame >= 6.0:
        print('Aprovado no exame')
    else:
        print('Reprovado no exame!')
else:
    print('Aluno aprovado.')
