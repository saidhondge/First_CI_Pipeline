
"""Program 25: Find maximum and minimum in a list."""


def find_max_min(numbers):
    """Return maximum and minimum values from a list."""

    if not numbers:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    return maximum, minimum


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    try:
        maximum, minimum = find_max_min(numbers)
        print("Maximum:", maximum)
        print("Minimum:", minimum)
    except ValueError as error:
        print(error)
