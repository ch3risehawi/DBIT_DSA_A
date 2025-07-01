def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

# Example usage:
if __name__ == "__main__":
    print(find_max([1, 5, 3, 9, 2]))      # Output: 9
    print(find_max([]))                   # Output: None