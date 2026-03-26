n1 = [3,5,2,1,9,7,5,8]
lista = ['oi', True, 4.5, 34]
n2 = [] # criar lista vazia

lista.append('undaia') # adiciona valores no fim da lista
print(lista)

lista.insert(2, 'tralalero') # adiciona valores em algum index específico
print(lista)

print(lista[-1]) # mostra o último item da lista

lista.pop() # apaga o último valor da lista
print(lista)

lista.pop(1) # apaga valores da lista pelo index
print(lista)

lista.remove('oi') # remove item pelo conteúdo
print(lista)

print(len(n1)) # ver tamanho da lista

print(sorted(n1)) # mostrar do - ao +
print(sorted(n1, reverse=True)) # mostrar do + ao -

print(max(n1)) # maior valor da lista
print(min(n1)) # menor valor da lista

print(sum(n1)) # soma valores da lista

print(n1.index(3)) # mostra o index de determinado item
print("-="*10)
# como mostrar a lista inteira mais bonito
for a in range (len(n1)):
    print(n1[a], end=' -> ')

print("-="*10)
