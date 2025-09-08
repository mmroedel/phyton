""" 8.	Calculadora de Área: Escreva um programa que leia a largura e a altura de uma parede em metros,
 calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
   pinta uma área de 2m². """

base= int(input("Digite a largura da parede em metros: "))
altura= int(input("Digite a altura da parede em metros: "))
area= int(base*altura)

tinta=int(area/2)

print(f"A área total é {area}m² e serão necessários {tinta} litros de tinta para pintar essa parede!")