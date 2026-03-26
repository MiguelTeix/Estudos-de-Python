#senha = str(input("Digite a senha: "))

#if senha == 'guel':
#    print("senha correta, bem-vindo miguel")

#elif senha == 'ar1103':
#    print("senha correta, bem-vindo arthur")

#else:
#    print("Senha incorreta")


# Ler 3 notas e dependendo da média vai mostrar:
# media = 6 -> RECUPERAÇÃO
# media > 6 -> APROVADO
# media < 6 -> REPROVADO

n1 =  float(input("Digite a n1: "))
n2 =  float(input("Digite a n2: "))
n3 =  float(input("Digite a n3: "))
soma = n1 + n2 + n3 

if soma /3 == 6:
    print (" Recuperação")

elif soma /3 < 6:
    print ("Reprovado")

elif soma /3 > 6: 
    print ("Aprovado")