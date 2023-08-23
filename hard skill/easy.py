def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Bir sayı girin: "))
result = factorial(number)
print(f"{number} sayısının faktöriyeli: {result}")