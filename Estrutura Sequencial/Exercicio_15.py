"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
valor_hora = int(input("Digite o valor recebido por Hora trabalhada: "))
hora = int(input("Digite a quantidade de Horas trabalhadas: "))

salario_bruto = valor_hora * hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"""
+ Salário Bruto : {salario_bruto} R$
- IR (11%) : {ir} R$
- INSS (8%) : {inss} R$
- Sindicato ( 5%) : {sindicato} R$
= Salário Liquido : {salario_liquido} R$
""")