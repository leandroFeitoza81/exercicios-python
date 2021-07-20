"""
    Programa que recebe um número inteiro e
    calcula o dobro, o triplo e a raiz quadrada.
"""

number = int(input("Digite um número: "))
double = number * 2
triple = number * 3
sqrt = number ** (1 / 2)
print(f'Número digitado: {number}')
print(f'Dobro ==> {double:5}')
print(f'Triplo ==> {triple:5}')
print(f'Raiz Quadrada ==> {sqrt:5}')
