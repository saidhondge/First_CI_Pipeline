
"""Program 27: Rotate a list by k positions."""


def rotate_list(items, k):
    """Rotate a list right by k positions."""
    if not items:
        return []

    k = k % len(items)

    return items[-k:] + items[:-k] if k else items.copy()


if __name__ == "__main__":
    items = list(map(int, input("Enter list elements: ").split()))
    k = int(input("Enter rotation value: "))

    print("Rotated list:", rotate_list(items, k))
