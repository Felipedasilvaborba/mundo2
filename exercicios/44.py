print('=========LOJA DO FELIPE=========')
valor=float(input('Qual valor do produto? R$'))
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço normal ')
print('[4] 3x ou mais no cartão: 20% de juros')
pagamento=int(input('Selecione a forma de pagamento: '))
if pagamento == 1:
    desconto = valor - ((valor*10)/100)
    print('O valor de R${} com desconto fica R${}'.format(valor,desconto))
elif pagamento == 2:
    desconto = valor - ((valor*5)/100)
    print('O valor de R${} com desconto fica R${}'.format(valor,desconto))
elif pagamento == 3:
    print('O valor em 2x no cartão fica R${} com 2 parcelas de R${}'.format(valor,valor/2))
elif pagamento == 4:
    vezes=int(input('Em quantas vezes você deseja fazer o pagamento? '))
    juros = valor + ((valor*20)/100)
    print('O valor de R${} com o juros fica R${} com {} parcelas de R${}'.format(valor,juros,vezes,juros/vezes))
else:
    print("Forma de pagamento inexistente!!")