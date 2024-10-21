# 3. Análise de Faturamento Diário

import json

dados_json = '''
{
    "faturamento_diario": [0, 1500.50, 3000.00, 0, 2500.75, 4500.00, 0, 5000.00, 2000.00, 3500.25, 0, 0, 1800.00, 3200.00, 0, 4200.50]
}
'''

dados = json.loads(dados_json)
faturamento_diario = dados["faturamento_diario"]
faturamento_valido = [f for f in faturamento_diario if f > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)
dias_acima_da_media = sum(1 for f in faturamento_valido if f > media_faturamento)

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
