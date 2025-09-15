""""
5-Maior de três números
Ler três números e mostrar o maior deles.
"""
n1 = float(input("Insira um número: "))
n2 = float(input("Insira um segundo número: "))
n3 = float(input("Insira um terceiro número: "))
maior = n1

if n2>n1:
    maior = n1
if n3>maior: 
    maior=n3 
print(f"O maior número é o {maior}!")

