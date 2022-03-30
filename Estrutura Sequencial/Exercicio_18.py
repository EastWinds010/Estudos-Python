"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet 
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanho = int(input("Digite o Tamanho do Arquivo (MB): "))
velocidade = int(input("Digite a Velocidade (Mbps)"))

tempo = (tamanho/velocidade)/60

print(f"Tempo nececessário para download: {tempo} minutos")