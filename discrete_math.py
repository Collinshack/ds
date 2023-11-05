def count_numbers_with_digit_1(start, end):
    count = 0
    for num in range(start, end + 1):
        if '1' in str(num):
            count += 1
    return count

start_range = 1
end_range = 10_000_000

total_count = count_numbers_with_digit_1(start_range, end_range)
print("Total count of numbers with the digit '1' in the range:", total_count)