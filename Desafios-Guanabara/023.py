num = int(input('Digite um numero (0-9999) -> '))
unidade = num % 10
num /= 10
dezena = num % 10
num /= 10
centena = num % 10
num /= 10
milhar = num % 10
print('unidade = {}' .format(int(unidade)))
print('Dezena = {}' .format(int(dezena)))
print('Centena = {}' .format(int(centena)))
print('Milhar = {}' .format(int(milhar)))
