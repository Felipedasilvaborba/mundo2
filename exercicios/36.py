casa=int(input('Qual valor do imovel que você deseja comprar? R$'))
salario = float(input('Qual sálario do comprador? R$'))
financiamento=int(input('Em quantos anos você quer financiar? '))
prestação = casa / (financiamento * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${} em {} anos'.format(casa,financiamento))
print('O valor da prestação ficará R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Financiamento concedido')
else:
    print('Financiamento Negado!!!')