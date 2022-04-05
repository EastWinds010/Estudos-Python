"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
popA = int(input("População País A: "))
taxaA = float(input("Taxa de Crescimento País A: "))/100
popB = int(input("População País B: "))
taxaB = float(input("Taxa de Crescimento País B: "))/100
n= 0

while popA <= popB:
    popA = popA + (popA*taxaA)
    popB = popB + (popB*taxaB)
    n = n+1
print(f"Levará {n} anos para a População do País A Atingir a População do País B")