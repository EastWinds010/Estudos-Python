"""Exercício 7.Faça um Programa que calcule a área de um quadrado, em seguida mostre
o dobro desta área para o usuário.
"""

l = int(input('Digite a medida do lado do quadrado: '))

area= l*l 
darea = area*2

print(f"""
A área do quadrado é: {area}
O dobro da área é: {darea}
""")