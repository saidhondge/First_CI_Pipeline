
"""Program 26: Find the sum of all elements in a list."""


def sum_of_list(numbers):
    """Return the sum of all numbers in the list."""
    total = 0

    for number in numbers:
        total += number

    return total


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print("Sum of list:", sum_of_list(numbers))
