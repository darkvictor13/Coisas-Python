frase = input('Digite uma frase : ').strip().upper()
print('A letra [A ou a] aparece {} vezes' .format(frase.count('A')))
print('Primeira aparicao = {}* letra' .format(frase.find('A') + 1))
print('Ultima aparicao = {}* letra' .format(frase.rfind('A') + 1))
