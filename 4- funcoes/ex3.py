# quero uma funcao voto e em voto vou colocar um ano
# se o ano for menor que 16 anos, vai me mostrar que seu voto é proibido
# se for entre 16 e 18 seu voto é opcional
# se for maior que 70 seu voto é opcional
# se for maior que 18 seu voto é obrigatório]
# se eu nao colocar nenhum valor vai me mostrar 2008
# "Voce tem x anos e seu voto é: "


def voto(ano):
    idade = 2026 - ano

    if idade < 16:
        print (f'Você tem {idade} anos e seu voto é Proibido ')

    elif idade >= 16 and idade < 18:
        print (f'Você tem {idade} anos e seu voto é Opcional ')

    elif idade >= 70:
        print (f'Você tem {idade} anos e seu voto é Opcional ')
    
    elif idade >= 18 and idade < 70:
        print (f'Você tem {idade} anos e seu voto é Obrigatório')
voto(2002)
voto(1900)
voto(2010)
voto(2020)