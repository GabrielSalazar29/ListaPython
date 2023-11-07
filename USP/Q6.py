preco_ingresso = 5.0
lucro_maximo = 0
preco_maximo = 0
qtd_vendidos_maximo = 0

while preco_ingresso >= 1.0:
    qtd_vendidos = 120 + (preco_ingresso - 5.0) * 26
    receita = qtd_vendidos * preco_ingresso
    despesas = 200
    lucro = receita - despesas

    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_maximo = preco_ingresso
        qtd_vendidos_maximo = qtd_vendidos

    print(f"Preço do ingresso: R${preco_ingresso:.2f}, Lucro: R${lucro:.2f}")
    preco_ingresso -= 0.5

print(f"Lucro máximo esperado: R${lucro_maximo:.2f}")
print(f"Preço do ingresso para o lucro máximo: R${preco_maximo:.2f}")
print(f"Quantidade de ingressos vendidos para o lucro máximo: {qtd_vendidos_maximo}")