#bolus de correção
print('Bolus de Correção (BC):\n'
'quantidade de insulina rápida ou ultra-rápida\n'
'necessária para a correção da glicemia antes\n'
'das refeições, calculada de forma individual\n'
'através do Fator Sensibilidade (FS).')
gm = float(input('Glicemia do Momento:\n'))
mg = float(input('Metea de Glicemia:\n'))
fs = float(input('Fator de Sencibilidade:\n'))
bc = (gm - mg)/ fs

print(f'O Bolus de correção é {bc} UI.')