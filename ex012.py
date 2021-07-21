"""
    Programa verifica se letra digitada
    é uma vogal ou consoante
"""
str_input = input("Digite uma letra qualquer: ")
character = str.lower(str_input)
vogais = "aeiou"
if character in vogais:
    print("Caracter digitado é uma vogal")
else:
    print("Caracter digitado é uma consoante")
