"""
Exercicio 13: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
h = int(input("Digite sua altura: "))

pesoH = (72.7*h) - 58
pesoM = (62.1*h) - 44.7

print(f"""
Peso ideal para Homens: {pesoH}
Peso ideal para Mulheres: {pesoM}
""")