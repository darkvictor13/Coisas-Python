import random
print('Informe o nome de 4 alunos')
nome1 = input('Primeiro nome : ')
nome2 = input('Segundo nome : ')
nome3 = input('Terceiro nome : ')
nome4 = input('Quarto nome : ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O escolhido foi {}' .format(escolhido))
