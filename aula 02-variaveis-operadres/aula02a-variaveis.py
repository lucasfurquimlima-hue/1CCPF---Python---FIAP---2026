import random

print("fala ai galera!")

print(7 + 4)
print("7 + 4")
print("7" + "4") #CONCATENAÇÃO DE STRINGS

# comentarios de 1 linha
'''
Comentários de multiplas linhas 

'''

#variaveis
nome = "lucas"
idade = 18
peso = 70

print(nome, idade, peso)
print(f"ola, {nome}!")

# INPUT -- SIMULA FORMS NO CMD
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso: "))

print(nome, idade, peso)

#DESAFIO
#1
nome = input("digite seu nome")
print(f"Bem Vindo {nome}!")

#2
Dia = input("digite o dia do seu nascimento")
Mes = input("digite o mes que voce nasceu")
Ano = input("digite o ano que voce nasceu")

print(Dia, Mes, Ano)

#3
numero1 = random.randint(1, 100)
numero2 = random.randint(1, 100)
soma = numero1 + numero2
print(f"o primeiro numero foi: {numero1}")
print(f"o segundo numero foi: {numero2}")
print(f"a soma total é: {soma}")
