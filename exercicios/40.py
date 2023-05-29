n1=float(input('Digite a primeira nota do aluno: '))
n2=float(input('Digite a segunda nota do aluno: '))
media = (n1+ n2) / 2
if media >= 7:
    print('Sua média foi {:.2f} PARABÉNS você foi APROVADO!!'.format(media))
elif media < 7 and media > 5:
    print('Sua média foi {} você está em RECUPERAÇÃO!!'.format(media))
else:
     print('Sua média foi {} você está REPROVADO!!'.format(media))