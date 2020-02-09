import random
print('Informe o nome de 4 alunos')
nome1 = input('Primeiro nome : ')
nome2 = input('Segundo nome : ')
nome3 = input('Terceiro nome : ')
nome4 = input('Quarto nome : ')
matriz = [nome1, nome2, nome3, nome4]
random.shuffle(matriz)
print('Ordem de apresentacao eh : \n [{}]' .format(matriz))
