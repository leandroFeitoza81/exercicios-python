""" Programa recebe um número inteiro
    E mostra o seu antecessor e seu sucessor.
"""
while True:
    try:
        number = int(input('Digite um número inteiro: '))
    except ValueError:
        print("Valor inválido ")
    else:
        break

print(f'O antecessor de {number} é {number - 1} e seu sucessor é {number + 1}')
