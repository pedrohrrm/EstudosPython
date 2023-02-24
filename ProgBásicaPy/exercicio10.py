alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
alunos
with open('alunos.txt', 'w') as text:
    for aluno, nota in alunos.items():
        text.write(f'{aluno}, {nota}\n')
with open('alunos.txt', 'r') as text:
    for linha in text:
        print(linha)