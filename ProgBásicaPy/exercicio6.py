import numpy as np
# lista = []
# for _ in range (1,6):
#     valor = int(input('Digite o valor: '))
#     lista.append(valor) #esse comando adiciona um item na lista apos entrarmos com o valor.
# print(lista)

# soma = 0
# for i in range(len(lista)): #len vai indicar o tamanho da lista.
#     soma += lista[i]
# print('Soma: ', soma)

#DICIONARIOS

# alunos = {}
# for _ in range(1, 4):
#   nome = input('Digite o nome: ')
#   nota = float(input('Digite a nota: '))
#   alunos[nome] = nota 
#   alunos['maria'] #Traz a nota do aluno de nome maria.
#   alunos.values() #Traz as notas de todos os alunos cadastrados.

#   soma = 0
# for nota in alunos.values():
#   #print(nota)
#   soma += nota
# print('Média: ', soma / 3) #esse for irá calcular a média, como nos exemplos anteriores.

# MATRIZ

matriz = np.array([[3,4,1],[3,1,5]])

matriz.shape

soma=0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
print('Soma: ', soma)