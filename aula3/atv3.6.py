"""
6-Cálculo do salário líquido
Ler o salário bruto de um funcionário e calcular o salário líquido com desconto de 10%. (0.10)
"""

sb=float(input("Para realizar o cálculo do seu salário líquido, informe o seu salário bruto: "))
sl=sb-(sb*0.10)
print(f"Seu salário líquido é de R${sl}.")