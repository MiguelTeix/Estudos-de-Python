# Quantidade de numeros digitados
# O maior e menor num digitados
# Soma dos núm e a média


def valores(*numerinhos):
    print (f'O maior numero digitado foi: {max(numerinhos)}')
    print (f'O menor numero digitado foi: {min(numerinhos)}')
    print (f'A soma dos numeros digitados é: {sum(numerinhos)}')
    print (f'A média dos numeros digitados é: {sum(numerinhos)/len(numerinhos)}')
    print('_'*30)


valores(3,4,6,1,0,9,6)
valores(1,2,3)