#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.

#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.

#E calcular o total que será pago ao fim do parcelamento (juros 15% a.a)

#Resposta:
#Financiamento Aprovado
#Valor da casa: XXXXXX
#Salário: XXXXXXX
#Meses: XXXXXX
#Prestação: XXXXXXX
#Valor total devido: XXXXXXX 

valorcasa = (float(input("Informe o valor da casa: R$ ")))
salario = (float(input("Informe o salario do suposto comprador: R$ ")))
tempo = (int(input("Em quantos anos ele pretende pagar? ")))
juros = valorcasa*tempo*0.15
parcelas = int(tempo*12)
liberacao = (salario*0.30)

valorfinal = valorcasa + juros 
valorparcelas=(valorfinal/parcelas)

if valorparcelas>liberacao:
    print("EMPRÉSTIMO NEGADO")
else:
    print("-----------------EMPRÉSTIMO LIBERADO. PARABÉNS!-----------------------")

print(f" ----O valor total para o pagamente é de: R${valorfinal}")
print(f"O valor das parcelas será de R${valorparcelas:.2f} ")
print(f"---------A quantidade de parcelas solicitadas é de {parcelas}")
