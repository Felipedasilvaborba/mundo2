n=int(input('Escreva um número inteiro qualquer: '))
print('[1] para converter em Bínario \n[2] Para converter em OCTAL\n[3] Para converter em Hexadecimal\n')
opção=int(input('Selecione:'))

if opção == 1:
    print('{} convertido para BINARIO É {}'.format(n,bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL É {}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADEXIMAL É {}'.format(n,hex(n)[2:]))
else:
    print('Tente novamente')
    