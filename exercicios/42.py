n1=float(input('Digite o primero segmento: '))
n2=float(input('Digite o segundo segmento: '))
n3=float(input('Digite o terceiro segmento: '))
if n1 == n2 == n3:
    print('Com os Segmentos acima é POSSIVEL formar um triangulo EQUILÁTERO')
elif n1 > n2 + n3 or n2 > n1 + n3 or n3 > n1 + n2:
    print('com os Segmentos acima NÃO É POSSIVEL formar um triangulo')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Com os Segmentos acima é POSSIVEL formar um triangulo ISÓSCELES')
elif n1 // n2 or n1//n3 or n2 // n3:
    print('Com os Segmentos acima é POSSIVEL formar um triangulo ESCALENO')