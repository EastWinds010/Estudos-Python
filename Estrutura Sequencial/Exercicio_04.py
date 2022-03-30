#Exercício 4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.

media_1 = int(input('Digite a primeira Média: '))
media_2 = int(input('Digite a segunda Média: '))
media_3 = int(input('Digite a terceira Média: '))
media_4 = int(input('Digite a quarta Média: '))

operacao= (media_1 + media_2 + media_3 + media_4)/4

print(f"A média é {operacao}")
