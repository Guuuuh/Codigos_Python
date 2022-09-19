# Faça o fatorial de um número inserido pelo usuário
n = int(input("Insira um número para calcular seu fatorial: "))


def fatorial(n):
    return 1 if (n < 2) else n * fatorial(n - 1)


print(fatorial(n))
