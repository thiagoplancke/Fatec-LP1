# 3. Caixa registradora
# • Leia preços de produtos até que o usuário digite 0.
# • Calcule o valor total da compra e aplique desconto:
# • acima de R$100 → 10% de desconto
# • caso contrário → sem desconto.

produtos = ["feijão","arroz","leite","carne","maçã","Sabonete"]
x = 0
soma = 0
while x < len(produtos):
    preco = float(input(f"Digite o preço do(a) {produtos[x]}: R$"))
    soma += preco
    x += 1
    if preco == 0:
        break
valor_total = soma
if soma > 100:
    valor_total *= 0.90
    print(f"O valor total com desconto de 10% foi: R${valor_total}")
else:
    print(f"O valor total foi: R${valor_total}")