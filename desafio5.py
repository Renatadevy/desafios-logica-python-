# 5. Inversão de String Manualmente

string_inicial = input("Informe uma palavra: ")

string_invertida = ""

for i in range(len(string_inicial) - 1, -1, -1):
    string_invertida += string_inicial[i]  

print(f"String invertida: {string_invertida}")
