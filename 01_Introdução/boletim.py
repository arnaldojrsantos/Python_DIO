print ('Aqui você saberá se está aprovado, de recuperação ou reprovado, de acordo com a sua média pnderada.')
n1 = float(input('Digite a primeia nota.\n'))
n2 = float(input('Digite a segunda nota.\n'))
n3 = float(input('Digite a terceira nota.\n'))
n4 = float(input('Digite a quarta nota.\n'))

m = (n1*1 + n2 *2 + n3*3 + n4*4)/ (1+2+3+4)

if m >= 7:
    print(f'Sua média é {m:.2f}.\n'
          'Você está aprovado!')
elif m < 7 and m >= 4:
    print(f'Sua média é {m:.2f}.\''
          'Você está de recuperação')
else:
    print(f'sua média é {m:.2f}.\n'
          'Você está reprovado!')