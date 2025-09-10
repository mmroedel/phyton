anonascimento = int(input("Digite o ano em que você nasceu (utilizando quatro digitos. Por exemplo: '1945'): "))

from datetime import date

ano_atual = date.today().year
idade = ano_atual - anonascimento
print(f"Sua idade é {idade}")
if idade >= 18:
    print("Seu voto é Obrigatório")
elif idade >=16:
    print("Seu voto é Opcional")
else: 
    print("Voto Negado")