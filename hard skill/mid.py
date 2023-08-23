def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    else:
        return total / count

num_list = []
n = int(input("Kaç tane sayı gireceksiniz? "))
for i in range(n):
    num = float(input(f"{i+1}. sayıyı girin: "))
    num_list.append(num)

average = calculate_average(num_list)
print(f"Girilen sayıların ortalaması: {average}")