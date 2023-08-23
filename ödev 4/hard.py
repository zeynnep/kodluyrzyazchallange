def find_divisors_sum(number):
    divisors_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum

user_input = int(input("Bir sayı girin: "))
divisors_sum = find_divisors_sum(user_input)
print(f"{user_input} sayısının tam bölenlerinin toplamı: {divisors_sum}")