peso=float(input('Digite seu peso em Kg: '))
altura=float(input('Digite sua altura em metro: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu IMC é {:.2f} Você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} Você está no peso Ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} Você está sobre peso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} Você está com obesidade'.format(imc))
else:
    print('Seu IMC é {:.2f} Você está com obesidade mórbida'.format(imc))