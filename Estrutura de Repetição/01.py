"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja 
inválido e continue pedindo até que o usuário informe um valor válido.
"""
n = int(input("Digite um número de 0 a 10: "))

while n <=0 or n >=10:
    print("O número digitando é INCORRETO")
    n = int(input("Digite um número de 0 a 10: "))

print("Número digitado CORRETAMENTE")