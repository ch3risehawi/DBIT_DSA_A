def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Example usage:
if __name__ == "__main__":
    print(linear_search(['a', 'b', 'c'], 'b'))  # Output: 1
    print(linear_search([10, 20, 30], 25))      # Output: -1