#7.	Conversor de Moedas: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (considere um valor fixo para o dólar).
conta= float(input("Olá! Favor informar o valor (em reais) atual presente na carteira para a conversão: R$ "))
valor= float(conta/5.60)

print(f"Você pode comprar até ${valor} em dólares")