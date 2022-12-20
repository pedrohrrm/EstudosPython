for numero in range(1,5):
    print(numero)

for numero in range(5, 0, -1):
    print(numero)

# SOMATÓRIO:

soma = 0
for numero in range(1, 6):
    print(numero)
    soma = soma + numero
    print(soma)

palavra = 'sorvete'
for letra in palavra:
    print(letra)
    if letra == 'v':
        print('Letra v encontrada.')

# FOR ANINHADO:

for i in range (0, 5):
    print(i)
    print('----')
    for j in range (0, 3):
        print(j)
    print()