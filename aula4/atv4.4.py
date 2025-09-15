"""

4-Desconto por valor da compra
	Ler o valor de uma compra:	
	Se for maior que 100, dar 10% de desconto.
	Senão, não dar desconto.

"""
compra = (float(input("Digite o valor de sua compra: ")))
compradesconto=compra-(compra*0.10)

if compra>100:
    print(f"O valor da sua compra com 10% de desconto é R${compradesconto} ")
else:
    print(f"O valor da sua compra é R${compra:.2f} ")