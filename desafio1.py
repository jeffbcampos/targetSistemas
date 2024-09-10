def esta_na_sequencia_fibonacci(numero):
    primeiro = 0
    segundo = 1
    while primeiro <= numero:
        if primeiro == numero:
            return True
        proximo = primeiro + segundo        
        primeiro = segundo
        segundo = proximo
    return False

numero_informado = int(input("Informe um número para verificar na sequência de Fibonacci: "))

if esta_na_sequencia_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
