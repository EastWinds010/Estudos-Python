"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
login = input("Digite o Login: ")
senha = input("Digite a Senha: ")

while login == senha:
    print("Login e Senha não podem ser iguais")
    login = input("Digite o Login: ")
    senha = input("Digite a Senha: ")

print("Login Realizado com Sucesso")