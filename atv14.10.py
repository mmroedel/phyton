"""
10-Tarifa de energia
Ler o consumo em kWh:

Se for até 100, cobrar R$ 0,50 por kWh.

Se for acima de 100, cobrar R$ 0,70 por kWh.
"""

consumo = (float(input("Qual foi o consumo de energia? ")))

baixo = consumo * 0.50
alto = consumo * 0.70

if consumo > 100:
    print(f"O valor do Kw/h é R$0.70 e o valor total foi de R${alto}")
else: 
    print(f"O valor do Kw/h é R$0.50 e o valor total foi de R${baixo}")