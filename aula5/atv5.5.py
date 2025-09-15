
#maior e menor da sequência: faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos:
peso = [ ]
for x in range(5):
    x=(float(input(f"Digite o peso da {x+1}ª pessoa: ")))
    peso.append(x)
peso_ordenado = sorted(peso)
print(f"O maior peso lido é {peso_ordenado[4]} e o menor peso lido é {peso_ordenado[0]}.")
