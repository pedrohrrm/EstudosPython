# n1 = int(input('Digite a Nota 1 :'))
# n2 = int(input('Digite a Nota 2 :'))
# n3 = int(input('Digite a Nota 3 :'))
# n4 = int(input('Digite a Nota 4 :'))
# n5 = int(input('Digite a Nota 5 :'))

# media = (n1 + n2+ n3+ n4+ n5) / 5
# print('A média é: ')
# print(media)

nota = media = soma = 0
print(nota, media, soma)

for _ in range(1, 6):
    nota = float(input('Digite a nota:'))
    soma += nota
    print(soma)
    media = soma/5
    print('A média é: ', media)

# TABUADA DO 3

# numero = 3
# multi = 0
# while numero >= 0 or numero == 10:
#     tabuada = numero*multi
#     print (tabuada)
#     multi +=1

multi = 0
for numero in range (0, 11):
    tabuada = multi * 3
    print(multi, 'X 3 = ', tabuada)
    multi += 1