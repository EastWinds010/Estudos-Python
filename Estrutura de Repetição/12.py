"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
"""
numero = int(input("Digite um número:"))
n = 1
while n <= 10:
    mult = numero*n
    print(f" {numero}x{n} = {mult} ")
    n = n + 1
