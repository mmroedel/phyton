"""
9-Aumento de salário
Ler o salário de um funcionário:

Se for menor que 2000, aumentar em 15%.

Senão, aumentar em 10%.
"""

salario = (float(input("Informe o valor do seu salário: ")))

if salario < 2000:
    print(f" O seu salário é  de R$ {salario*1.15} ")
else:
    print(f" O seu salário é  de R$ {salario*1.10} ")