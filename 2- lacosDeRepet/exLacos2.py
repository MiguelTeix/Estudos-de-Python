# usando while, peça números infinitas vezes até o usuário não querer mais digitar
# após ler todos os números, diga a soma dos números digitados

total = 0
while True: 
    n = float(input("Digite um número: "))

    total += n 

    t = str(input("Quer continuar? "))
    
    if t == "Não":
        break 
    elif t == "Sim":
        continue 

print (f"A soma dos números digitados é {total}")