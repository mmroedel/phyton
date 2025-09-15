"""
7-Cálculo de IMC
Ler peso e altura, calcular o IMC e verificar:

	IMC < 18,5 → Abaixo do peso

	IMC entre 18,5 e 24,9 → Normal

	IMC ≥ 25 → Acima do peso
"""

nome =input("Qual seu nome? ")
altura = float(input("Insira a sua altura: "))
peso = float(input("Insira o seu peso: "))

imc= peso /(altura**2)

if imc<18.5:
    print(f"{nome}, seu IMC é de {imc:.2f} e você está Abaixo do peso.")
elif imc<24.9:
    print(f"{nome}, seu IMC é de {imc:.2f} e  você está com peso normal.")
else:
    print(f"{nome}, seu imc é de {imc:.2f} e você está acima do peso.")