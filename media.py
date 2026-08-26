nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

media =(nota1 + nota2 + nota3 + nota4) /4

if media >=5: 
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")