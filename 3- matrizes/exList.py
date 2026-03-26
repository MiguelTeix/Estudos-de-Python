# Crie duas listas, uma vai se chamar alunos e a outra vai se chamar notas (ilimitadamente)
# vai pedir primeiro o nome e depois a nota SEMPRE
# ao final quero saber qual foi a maior e menor nota e DE QUEM FOI + média das pessoas

print("~"*30)
print("SISTEMA DE NOTAS".center(30))
print("~"*30)

alunos = []
notas = []

while True:
    alunos.append(str(input('Nome do aluno: ')))
    notas.append(int(input('Diga a nota: ')))

    resp = str(input("Quer continuar? "))

    if resp == 'Não':
        break

    print('-'*15)

print('-'*45)
print(f'{max(notas)} foi a maior nota e ela pertence a {alunos[notas.index(max(notas))]}')
print(f'{min(notas)} foi a menor nota e ela pertence a {alunos[notas.index(min(notas))]}')
print(f'a média das notas digitadas foi: {sum(notas)/len(notas)}')