"""
    Programa recebe um número inteiro e mostra a tabuada
"""
number = int(input('Digite um número inteiro: '))
for factor in range(11):
    print(f'{number} X {factor} = {factor * number} ')
