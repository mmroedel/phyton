#jogo de adivinhação
#Crie um jogo onde o utilizador advinha um numero de 1 a 100.

import random
numero_secreto = random.randint(1,10)
contador = 0

palpite = (int(input("Estou pensando em um número de 1 a 10, você consegue advinhar? ")))
while palpite != numero_secreto:
    print(f"Você errou. O número era {numero_secreto}. Tente novamente.")
    
    break
if palpite==numero_secreto:
    print("Você ganhou!")