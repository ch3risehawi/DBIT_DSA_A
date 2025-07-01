def find_min(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst[1:]:
        if num < min_value:
            min_value = num
    return min_value

# Example usage:
if __name__ == "__main__":
    print(find_min([7, 3, 5, 1, 8]))      # Output: 1
    print(find_min([]))                   # Output: None