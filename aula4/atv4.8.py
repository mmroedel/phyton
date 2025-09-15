"""
8-Maior e diferença
Ler dois números e mostrar qual é o maior e também a diferença entre eles."""

n1 = float(input("Insira um número: "))
n2 = float(input("Insira outro número: "))

if n1>n2:
    print(f"O maior número é o {n1} e a diferença entre eles é de {(n1-n2)}.")
else:
    print(f"O maior número é o {n2} e a diferença entre eles é de {(n2-n1)}")