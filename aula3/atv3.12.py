"""
12-Velocidade média
Ler a distância percorrida e o tempo gasto, depois calcular a velocidade média.
Fórmula: Vm = distância / tempo
por: Murilo Roedel
"""
distancia=(int(input("Informe, em metros, a distância percorrida: ")))
tempo=(float(input(f"Informe, em minutos, quanto tempo você levou para percorrer {distancia} metros: ")))
seg = tempo*60
vm= distancia/seg
print(f"Parabéns, sua velocidade média no percurso foi de {vm:.2f} m/s.")