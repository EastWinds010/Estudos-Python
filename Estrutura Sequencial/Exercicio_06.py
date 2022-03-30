"""Exercício 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
     A= 3,14 * r²
"""
r = int(input('Digite o raio do círculo em Metros: '))

pi= 3.1415926535898

operacao = pi* (r * r)

print(f"A área do círculo é: {operacao} Metros")