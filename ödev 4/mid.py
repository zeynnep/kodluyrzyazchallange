def find_min_max_numbers(arr):
    if not arr:
        return None, None  # Dizi boşsa en büyük ve en küçük değer yok

    min_num = arr[0]
    max_num = arr[0]

    for num in arr:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num

numbers = [int(x) for x in input("Diziyi girin (virgülle ayırarak): ").split(",")]
min_number, max_number = find_min_max_numbers(numbers)

if min_number is None or max_number is None:
    print("Dizi boş.")
else:
    print(f"En küçük sayı: {min_number}")
    print(f"En büyük sayı: {max_number}")