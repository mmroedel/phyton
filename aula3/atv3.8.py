""""
8-Cálculo da idade em dias
Ler a idade de uma pessoa em anos e calcular quantos dias ela já viveu (aproximando 1 ano = 365 
"""
nome=input("Qual seu nome? ")
idade=int(input(f"Olá, {nome}. Para descobrir quantos dias você já viveu? Então informe sua idade: "))

dias=(idade*365)
print(f"{nome}, você já viveu {dias} dias até hoje!")