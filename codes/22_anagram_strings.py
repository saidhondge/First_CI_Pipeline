"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    """Return True if two strings are anagrams."""
    first_clean = first.replace(" ", "").lower()
    second_clean = second.replace(" ", "").lower()

    return sorted(first_clean) == sorted(second_clean)


if __name__ == "__main__":
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    if is_anagram(str1, str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")