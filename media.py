nota1 = int(input("digite a sua nota: "))
nota2 = int(input("digite a sua nota: "))
nota3 = int(input("digite a sua nota: "))
nota4 = int(input("digite a sua nota: "))

media = (nota1+nota2+nota3+nota4)/4

print("sua media é:",media)

if media <= 3:
    print("reprovado")
elif media <= 5:
    print("recuperaçao")
else:
    print("aprovado")