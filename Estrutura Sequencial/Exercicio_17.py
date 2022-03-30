"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
arredonde os valores para cima, isto é, considere latas cheias.
"""
import math
area = int(input("Digite a área (m²) a ser pintada: "))

litros_tinta = area / 6 + ((area / 6)*0.10)
lata = math.ceil(litros_tinta / 18)
valor_lata = lata * 80
galao = math.ceil(litros_tinta / 3.6)
valor_galao = galao * 25
#Misto de Latas e Galões
mlatas = litros_tinta // 18
mgalao = (litros_tinta - (mlatas * 18)) // 3.6
valor = (mlatas*80) + (mgalao*25)

print(f"""
Área a ser pintada: {area}m²
--------------------------------------
Utilizando Apenas Latas de 18 Litros  
Quantidade de Latas: {lata}
Valor: {valor_lata} R$
--------------------------------------
Utilizando Apenas Galões de 3,6 Litros
Quantidade de Galões: {galao}
Valor: {valor_galao} R$
--------------------------------------
Utilizando Misto de Latas e galões
Quantidade de Latas: {mlatas}
Quantidade de Galões: {mgalao}
Valor: {valor} R$
""")