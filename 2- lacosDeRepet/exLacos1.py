# usando for faça um contador que o usuário decida:
# o início, o fim e o passo

n1 = int(input("Inicio: "))
n2 = int(input("Fim: "))
n3 = int(input("Passo: "))

for a in range (n1,n2  + 1,n3):
    print(f"{a}")