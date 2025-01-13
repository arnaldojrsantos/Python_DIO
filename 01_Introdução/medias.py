print('Vamos fazer a comparação entre média aritimética e ponderada')
n1 = float(input('Digite a primeia nota.\n'))
n2 = float(input('Digite a segunda nota.\n'))
n3 = float(input('Digite a terceira nota.\n'))
n4 = float(input('Digite a quarta nota.\n'))

mp = (n1*1 + n2 *2 + n3*3 + n4*4)/ (1+2+3+4)
ma = (n1 + n2 + n3 + n4)/4

if mp == ma:
    print(f'Sua média PONDERADA é {mp:.2f}. e sua média ARITIMÉTICA é {ma:.2f}\n'
          'As médias são iguais.')

elif mp > ma:
    print(f'Sua média PONDERADA é {mp:.2f}. e sua média ARITIMÉTICA é {ma:.2f}\n'
          f'Média Ponderada é mairo.')
else:
    print(f'Sua média PONDERADA é {mp:.2f}. e sua média ARITIMÉTICA é {ma:.2f}\n'
          f'Média Aritimética é maior.')