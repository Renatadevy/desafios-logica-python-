# 4. Percentual de Faturamento por Estado

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())

print("Faturamento mensal por estado:")
for estado, valor in faturamento.items():
    porcentagem = (valor / faturamento_total) * 100
    print(f"{estado}: R$ {valor:.2f} - {porcentagem:.2f}% do total")

print(f"\nFaturamento total: R$ {faturamento_total:.2f}")
