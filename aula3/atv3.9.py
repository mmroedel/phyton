#9-Resto da divisão
#Ler dois números inteiros e mostrar o quociente inteiro e o resto da divisão entre eles.

n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))
quociente=float(n1/n2)
resto = float(n1%n2)
print(f"O quiciente de {n1} dividido por {n2} é {int(quociente)} e o resto é {resto}.")