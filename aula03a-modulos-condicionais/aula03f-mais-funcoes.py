# FUNÇAO COM PARAMETRO SEM RETORNO
def boas_vindas(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

nome_digitado = input("Digite seu nome:")
boas_vindas(nome_digitado)

# funçao com parametro com retorno
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

print(soma(4, 3))
print(type(nome_digitado))

