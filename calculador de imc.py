print('\n\---- Índice de Massa Corporal ----/\n')
nome = input('Informe seu nome: ')


def calculo_imc(peso, altura):
    imc = peso / altura ** 2
    print('\n\---- Resultado ----/\n')
    print('Paciente {}, seu resultado foi:'.format(nome))
    print('IMC: {:.1f}. Diagnóstico:\n'.format(imc))
    if imc < 18.5:
         print('Você está abaixo do peso.\n')
    elif 18.6 <= imc <= 24.9:
         print('Você está no peso ideal. Parabéns!\n')
    elif 25 <= imc <= 29.9:
         print('Você está levemente acima do peso.\n')
    elif 30 <= imc <= 34.9:
         print('Você está com obesidade grau I.\n')
    elif 35 <= imc <= 39.9:
         print('Você está com obesidade grau II (severa).\n')
    else:
         print('Você está com obesidade grau III (mórbida).\n')

calculo_imc(float(input('Informe seu peso: ')), float(input('Informe sua altura: ')))
