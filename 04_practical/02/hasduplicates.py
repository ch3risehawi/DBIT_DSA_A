def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Example usage:
if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 2]))   # Output: True
    print(has_duplicates([1, 2, 3, 4]))   # Output: False