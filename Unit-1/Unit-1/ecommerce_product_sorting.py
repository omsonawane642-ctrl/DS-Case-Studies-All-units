"""E-commerce product sorting using Merge Sort (Divide and Conquer).

Educational example. No external packages are required.
"""


def merge_by_price(left, right):
    """Merge two price-sorted product lists into one sorted list."""
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["price"] <= right[j]["price"]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort_products(products):
    """Return products sorted by ascending price using Merge Sort."""
    if len(products) <= 1:
        return products[:]

    middle = len(products) // 2
    left_sorted = merge_sort_products(products[:middle])
    right_sorted = merge_sort_products(products[middle:])

    return merge_by_price(left_sorted, right_sorted)


def display_products(title, products):
    print(f"\n{title}")
    print("-" * 38)
    print(f"{'Product':<22} {'Price (INR)':>12}")
    print("-" * 38)
    for product in products:
        print(f"{product['name']:<22} {product['price']:>12,.2f}")


def main():
    products = [
        {"name": "Headphones", "price": 1499},
        {"name": "Keyboard", "price": 899},
        {"name": "Backpack", "price": 1199},
        {"name": "Mouse", "price": 499},
        {"name": "Monitor", "price": 7999},
    ]

    sorted_products = merge_sort_products(products)
    display_products("Original product catalog", products)
    display_products("Products sorted by ascending price", sorted_products)


if __name__ == "__main__":
    main()
