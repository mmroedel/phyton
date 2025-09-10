"""
1-Maior de dois números
Ler dois números e mostrar qual é o maior.
"""
n1 = float(input("Insira um número: "))
n2 = float(input("Insira outro número: "))

if n1>n2:
    print(f"{n1} é maior que {n2}!")
elif n1==n2:
    print(f"{n1} e {n2} são equivalentes!")
else: 
    print(f"{n2} é maior que {n1}!")

