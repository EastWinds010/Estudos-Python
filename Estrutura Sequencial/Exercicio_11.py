"""Exercício Exercício 11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        A - o produto do dobro do primeiro com metade do segundo .
        B - a soma do triplo do primeiro com o terceiro.
        C - o terceiro elevado ao cubo.
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro númweo inteiro: '))
num3 = int(input('Digite um número real: '))

calcA = 2*num1+(num2/2)

calcB = 3*num1+num3

CalcC = num3*num3

print(f"""
Resposta A: {calcA}
Resposta B: {calcB}
Resposta C: {CalcC}
""")