# Leia 3 valores do usuário e some os 2 maiores
a = int(input("Insira o primeiro valor: "))

b = int(input("Insira o segundo valor: "))

c = int(input("Insira o terceiro valor: "))


if a > b and a > c:
    maior1 = a
    if b > c:
        maior2 = b
    else:
        maior2 = c

if b > a and b > c:
    maior1 = b
    if a > c:
        maior2 = a
    else:
        maior2 = c

if c > b and c > a:
    maior1 = c
    if a > b:
        maior2 = a
    else:
        maior2 = b


def soma():
    total = maior1 + maior2
    return total


print(soma())
