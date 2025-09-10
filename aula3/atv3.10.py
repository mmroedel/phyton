"""10-Conversão de minutos em horas
Ler um valor em minutos e converter para horas e minutos.
Exemplo: 135 minutos → 2 horas e 15 minutos.
Por: Murilo Roedel
"""

min=int(input("Digite um valor em minutor para converter para horas: "))
horas=min//60 
minutos=min%60
print(f" {min} minutos, são equivalentes a {horas} hora(s) e {minutos} minuto(s).")