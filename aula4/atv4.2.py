"""
2-Positivo, negativo ou zero
Ler um número e informar se ele é positivo, negativo ou zero.
"""

n1 = float(input("Insira um número: "))

if n1>0:
    print(f"{n1} é Positivo!")
elif n1==0:
    print(f"{n1} é zero!")
else: 
    print(f"{n1} é Negativo!")

