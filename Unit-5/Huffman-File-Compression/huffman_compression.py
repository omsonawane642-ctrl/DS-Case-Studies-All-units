import heapq
from collections import Counter
from itertools import count


class Node:
    def __init__(self, frequency, character=None, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def build_huffman_tree(text):
    frequencies = Counter(text)
    if not frequencies:
        return None, frequencies

    serial = count()
    heap = []
    for character, frequency in frequencies.items():
        heapq.heappush(heap, (frequency, next(serial), Node(frequency, character)))

    while len(heap) > 1:
        left_frequency, _, left_node = heapq.heappop(heap)
        right_frequency, _, right_node = heapq.heappop(heap)
        parent = Node(left_frequency + right_frequency, None, left_node, right_node)
        heapq.heappush(heap, (parent.frequency, next(serial), parent))

    return heap[0][2], frequencies


def make_codes(root):
    codes = {}
    if root is None:
        return codes

    # A one-character input still needs a usable code.
    if root.is_leaf():
        codes[root.character] = "0"
        return codes

    def walk(node, prefix):
        if node.is_leaf():
            codes[node.character] = prefix
            return
        walk(node.left, prefix + "0")
        walk(node.right, prefix + "1")

    walk(root, "")
    return codes


def encode(text, codes):
    return "".join(codes[character] for character in text)


def decode(encoded_bits, root):
    if root is None:
        return ""
    if root.is_leaf():
        return root.character * len(encoded_bits)

    decoded = []
    node = root
    for bit in encoded_bits:
        node = node.left if bit == "0" else node.right
        if node.is_leaf():
            decoded.append(node.character)
            node = root
    return "".join(decoded)


def main():
    print("Huffman Coding - Educational Compression Demo")
    text = input("Enter text to encode: ")
    if not text:
        print("No text was entered.")
        return

    root, frequencies = build_huffman_tree(text)
    codes = make_codes(root)
    encoded_bits = encode(text, codes)
    decoded_text = decode(encoded_bits, root)

    print("\\nCharacter frequencies:")
    for character in sorted(frequencies):
        display_character = repr(character)
        print(f"{display_character}: {frequencies[character]}")

    print("\\nHuffman codes:")
    for character in sorted(codes):
        print(f"{repr(character)}: {codes[character]}")

    print("\\nEncoded bit string:")
    print(encoded_bits)
    print("\\nDecoded text:")
    print(decoded_text)

    # A simple comparison only; this is not the final size of a ZIP/GZIP file.
    fixed_width_bits = len(text) * 8
    print(f"\\nOriginal-size estimate at 8 bits/character: {fixed_width_bits} bits")
    print(f"Huffman encoded data: {len(encoded_bits)} bits")
    if fixed_width_bits:
        saving = (1 - len(encoded_bits) / fixed_width_bits) * 100
        print(f"Encoded-data bit-count difference: {saving:.2f}%")
    print("\\nNote: Tree/code storage and ZIP/GZIP file-format overhead are not included.")


if __name__ == "__main__":
    main()
