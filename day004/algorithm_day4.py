def count_even(nums):
    even_count = 0
    for n in nums:
        if n % 2 == 0:
            even_count += 1
    return even_count

def sum_even(nums):
    even_total = 0
    for n in nums:
        if n % 2 == 0:
            even_total += n
    return even_total

def main():
    test_cases = [
        [],
        [1, 3, 5],
        [1, 2, 3, 4],
        [2, 4, 6],
    ]
    for case in test_cases:
        print(f"{case} → 偶数个数: {count_even(case)}, 偶数总和: {sum_even(case)}")

main()