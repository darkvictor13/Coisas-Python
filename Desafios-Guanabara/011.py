print('Informe as dimensoes da sua parede')
largura = float(input('Largura : '))
altura = float(input('Altura : '))
area = largura * altura
print('Sua parede tem {:.1f} metros quadrados' .format(area))
print('Entao voce precisa de {:.1f} litros de tinta' .format(area / 2))
