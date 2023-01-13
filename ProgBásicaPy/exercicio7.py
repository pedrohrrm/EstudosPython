def lerTemperatura():
    temperatura = float(input('Digite a temperatura em Celsius: '))
    return temperatura

def converter(temperaturaCelsius):
    temperaturaFar = ( 9 * temperaturaCelsius + 160)/5
    return temperaturaFar

def mostrar(temperaturaFar):
    print(temperaturaFar)

temperaturaCels = lerTemperatura() #é a temperatura que o usuário vai digitar.
temperaturaFar = converter(temperaturaCels)
mostrar(temperaturaFar)