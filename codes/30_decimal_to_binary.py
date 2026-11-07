"""Program 30: Convert decimal number to binary."""


def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Number cannot be negative")

    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    return binary


if __name__ == "__main__":
    number = int(input("Enter a decimal number: "))
    print("Binary number:", decimal_to_binary(number))