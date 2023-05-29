nascimento=int(input('Qual ano você nasceu? '))
idade = 2023 - nascimento
alistamento = 18
if idade == alistamento:
    print('Você nasceu em {} você tem {} anos'.format(nascimento,idade))
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < alistamento:
    print('Você nasceu em {} você tem {} anos'.format(nascimento,idade))
    print('Falta {} anos para seu alistamento'.format(alistamento-idade))
    print('Seu alistamento será em {}'.format(2023+(alistamento-idade)))
else:
    print('Você nasceu em {} você tem {} anos'.format(nascimento,idade))
    print('você já se alistou a {} anos'.format(idade-alistamento))
    print('Seu alistamento foi em {}'.format(2023-(idade-alistamento)))