#contagem regressiva:
# mostre uma contagem regressiva para a queima de fogos, indo de 10 até 0 com pausa de 1 segundo entre eles:
import time
for numero in range(10,-1,-1):
    print(numero)
    time.sleep(1)
if numero==0:
    print("Feliz Ano novo!")