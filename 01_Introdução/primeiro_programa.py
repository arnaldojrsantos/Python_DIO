print('Hello, World!')

nome = input('Informe seu nome.\n')
print (f'Olá, {nome}!\n'
'Seja bem vindo!')
a = int(input('Digite um número:\n'))
b = int(input('Digite outro número:\n'))

soma = a + b

print(f'A soma entre {a} e {b} é {soma}.')

c = int(input('Digite outro número:\n'))
if c %2 == 0:
    print(f'{c} é um número par')
else:
    print(f'{c} é impar')

print('-'*20)
print('Agora vamos ver se as medidas escolhidas por você vão formar um triângulo:\n')
l1 = int(input('Digite o primeiro lado:\n'))
l2 = int(input('Digite o segundo lado:\n'))
l3 = int(input('Digite o terceiro lado:\n'))

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2 :
    print('Triangulo formado')
else:
    print('Triângulo não fomado')
peso = float(input('Digite o seu peso:\n'))
altura= float(input('Informe sua altura em m:\n'))

imc = peso/altura**2

print(f'Seu imc é: {imc:.3f}')

if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
else:
    print('Acima do peso.')