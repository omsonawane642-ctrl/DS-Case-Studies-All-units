# Case Study 2: ZIP/GZIP File Compression Using Huffman Coding

## Introduction
Files can contain repeated characters or symbols. Frequency-based encoding gives shorter bit codes to symbols that appear more often and longer codes to symbols that appear less often. Huffman coding is a lossless compression method that builds a binary tree from symbol frequencies.

ZIP and GZIP are file-compression formats that can use DEFLATE, which combines LZ77 and Huffman coding. This program demonstrates the Huffman-tree part for learning; it does not create actual `.zip` or `.gz` files.

## Aim
To understand frequency-based encoding and implement a Huffman tree to encode and decode text.

## Objectives
- Count how often each character appears.
- Build a Huffman tree using a priority queue.
- Generate prefix-free binary codes.
- Encode text and decode it back.
- Compare the encoded bit count with a simple 8-bit-per-character baseline.

## Problem Statement
Storing every character using a fixed number of bits can use more space than needed for data with uneven character frequencies. The program uses Huffman coding to assign shorter codes to frequent characters and longer codes to less frequent characters.

## Theory
A Huffman tree is built by repeatedly combining the two nodes with the lowest frequencies. The new node's frequency is the sum of the two selected frequencies. This continues until only one root node remains. The path from the root to each leaf gives that character's code: left edges represent `0` and right edges represent `1`.

Because Huffman codes are prefix-free, a code for one character is not the prefix of another character's code. This allows decoding without needing separators between codes.

## Algorithm
1. Count the frequency of every character in the input text.
2. Create one leaf node for each character and put the nodes in a min-priority queue.
3. Remove the two nodes with the smallest frequencies.
4. Combine them into a new parent node and add it back to the queue.
5. Repeat until one tree remains.
6. Traverse the tree to create codes.
7. Replace each character with its code to encode the text.
8. Traverse the tree according to the encoded bits to decode the text.

## Pseudocode
```text
HUFFMAN(frequencies):
    create a leaf node for each character
    add all leaf nodes to a min-priority queue

    while queue has more than one node:
        left = remove node with smallest frequency
        right = remove node with next-smallest frequency
        parent = new node with frequency left + right
        parent.left = left
        parent.right = right
        insert parent into queue

    return the remaining node as root
```

## How to Run
```bash
python huffman_compression.py
```

Enter a sample sentence when prompted. The program displays the character frequencies, Huffman codes, encoded bit string, decoded text, and a simple bit-count comparison.

## Complexity
For `n` characters of input and `k` distinct symbols, counting frequencies takes **O(n)**. Building the tree takes **O(k log k)**. Creating the encoded bit string takes **O(n)** plus the total number of output bits. The tree and code table require **O(k)** space, while the encoded output requires space proportional to its bit-string length.

## Important Note About ZIP/GZIP
This is an educational Huffman coding demonstration, not a full ZIP/GZIP compressor. Real DEFLATE-based ZIP/GZIP compression also uses LZ77-style matching and specific file-format headers, blocks, and checksums. The program's bit string is displayed as text for learning, so it is not itself a packed binary archive.

## Conclusion
In this case study, I learned how character frequencies can be used to build a Huffman tree. Frequent characters can receive shorter codes, which can reduce the total number of bits needed for some data. I also learned that real ZIP/GZIP compression uses more steps than Huffman coding alone.

## References
- Python documentation: https://docs.python.org/3/
- Huffman coding: standard data structures and algorithms study material.
- DEFLATE specification (RFC 1951): https://www.rfc-editor.org/rfc/rfc1951
