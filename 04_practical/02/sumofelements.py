def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total

#Example usage:
if __name__ == "__main__":
    print(sum_of_elements([1, 2, 3, 4]))  # Output: 10