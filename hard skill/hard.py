def count_target_occurrences(sorted_list, target):
    left_index = 0
    right_index = len(sorted_list) - 1

    first_occurrence = None
    last_occurrence = None

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if sorted_list[mid_index] == target:
            if mid_index == 0 or sorted_list[mid_index - 1] != target:
                first_occurrence = mid_index
                break
            else:
                right_index = mid_index - 1
        elif sorted_list[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    if first_occurrence is None:
        return 0  # Hedef sayı bulunamadı.

    left_index = first_occurrence
    right_index = len(sorted_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if sorted_list[mid_index] == target:
            if mid_index == len(sorted_list) - 1 or sorted_list[mid_index + 1] != target:
                last_occurrence = mid_index
                break
            else:
                left_index = mid_index + 1
        elif sorted_list[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    if last_occurrence is None:
        return 0  # Hedef sayı bulunamadı.

    occurrence_count = last_occurrence - first_occurrence + 1
    return occurrence_count

sorted_numbers = [int(x) for x in input("Sıralı bir sayı dizisi girin (virgülle ayırarak): ").split(",")]
target_number = int(input("Hedef sayıyı girin: "))
occurrences = count_target_occurrences(sorted_numbers, target_number)
print(f"{target_number}, dizide {occurrences} kez tekrar etti.")