# for = Para
# posso passar até 3 parâmetros

# 1 Parâmetro: vai do 0, até o número que eu coloquei -1
print("     1 parâmetro:")
for a in range(9):
    print(a)

print("-"*30)

# 2 Parâmetros: vai do 1º parâmetro, até o 2º que eu coloquei -1
print("     2 parâmetros:")

for miguel in range(1,11):
    print(miguel)

print("-"*30)

# 3 Parâmetros: vai do 1º até o 2º-1, pulando de 3ºp em 3ºp
print("     3 parâmetros:")

for a in range(1,11,2):
    print(a)

# ----------------------------------------------------------------------------
# while = Enquanto
contador = 0
while True:
    print('oi')
    contador +=1 
    if contador == 10:
        print(f"{contador} - chegamos no fim")
        break