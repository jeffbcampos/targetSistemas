def contar_letras_a(texto):    
    contador_a = 0    
    
    for letra in texto:
        if letra.lower() == 'a':
            contador_a += 1
    
    return contador_a

texto_teste = "Aqui está um exemplo de texto com algumas letras A."
resultado = contar_letras_a(texto_teste)
print("Quantidade de letras 'a':", resultado)
