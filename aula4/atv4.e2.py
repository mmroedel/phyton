"""
Caixa Eletrônico: Simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de R50,R20, R10 e R1 serão entregues.
"""
print("Seja bem-vindo! Cédulas disponíveis: R50,R20, R10 e R1 ")
valor = (int(input("Digite o valor que deseja sacar:R$ ")))

if valor%50==0:
    print(f"Você receberá {(valor//50)*1} notas de R$50 e {(valor%50)*1} notas de R$1.")
elif valor%20==0:
    print(f"Você receberá {(valor//20)*1} notas de R$20 e {(valor%20)*1} notas de R$1.")
elif valor%10==0:
    print(f"Você receberá {(valor//10)*1} notas de R$10 e {(valor%10)*1} notas de R$1.")
else:
    print(f"Você receberá {(valor//1)*1} notas de R$1.")


