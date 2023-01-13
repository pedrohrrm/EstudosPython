# Função sem parâmetro e sem retorno

def mensagem():
    print('Texto da função')


mensagem()
mensagem()
mensagem()

#Função com passagem de parâmetro


def mensagem(texto):
    print(texto)


mensagem('texto 1')
mensagem('texto 2')
mensagem('texto 3')


def soma(a, b):
    print(a + b)


soma(2, 3)
soma(3, 3)
soma(1, 2)

# Função com passagem de parâmetros e retorno


def soma(a, b):
    return a + b


soma(3, 2)
# r = 7
r = soma(3, 2)
print(r)


def calcula_energia_potencial_gravitacional(m, h, g=10):
    '''
    Calcula a energia potencial gravitacional
    Argumentos:
    m: massa, entrada como uma variável float
    h: altura, entrada como uma variável float

    Argumento opcional:
    g: aceleração gravitacional, com valor default de 10
    '''
    e = m * h * g
    return e


calcula_energia_potencial_gravitacional(30, 12)

calcula_energia_potencial_gravitacional(30, 12, 9.8)

help(calcula_energia_potencial_gravitacional)
