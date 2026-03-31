# Sem parâmetros

#def linha():
    #print("~"*20)

#def soma():
    #n1 = float(input("Digite um número: "))
    #n2 = float(input("Digite um número: "))
    #return n1 + n2

#linha()
#print(soma())
#linha()

# ====================================================

# Com parâmetros

def somar(*numeros):
    print(sum(numeros))

somar(3, 4, 5, 7)