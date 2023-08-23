def find_max_number(arr):
    max_num = arr[0]  # İlk elemanı başlangıçta en büyük olarak kabul ediyoruz
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

numbers = [int(x) for x in input("Diziyi girin (virgülle ayırarak): ").split(",")]
max_number = find_max_number(numbers)
print(f"En büyük sayı: {max_number}")