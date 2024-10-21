# 2. Verificar se um Número Pertence à Sequência de Fibonacci

numero_informado = int(input("Informe um número: "))

fib_1 = 0
fib_2 = 1
encontrado = False

while fib_1 <= numero_informado:
    if fib_1 == numero_informado:
        encontrado = True
        break
    fib_1, fib_2 = fib_2, fib_1 + fib_2

if encontrado:
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} NÃO pertence à sequência de Fibonacci.")
