notaA = float(input("Digite a 1 nota: "))
while notaA < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10")
    notaA = float(input("Digite a nota novamente: "))


notaB = float(input("Digite a 2 nota: "))
while notaB < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10")
    notaB = float(input("Digite a nota novamente: "))

media = (notaA + notaB) / 2
print(media)