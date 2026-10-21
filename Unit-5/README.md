Unit 5: GPS Navigation and Huffman Coding

Introduction

In this unit, I have studied two applications of data structures and algorithms. The first case study represents a city map as a weighted graph and finds the shortest route using Dijkstra's algorithm. The second case study explains file compression using character frequencies and a Huffman tree.

Aim

To understand the use of graph algorithms in GPS navigation and Huffman coding in data compression.

Objectives

- To understand weighted graphs and their applications.
- To represent a city map using vertices, edges, and weights.
- To implement Dijkstra's algorithm for finding the shortest route.
- To understand frequency-based encoding.
- To construct a Huffman tree and generate binary codes.
- To encode and decode text using Huffman coding.

Case Study 1: GPS / Navigation System Using a Weighted Graph

Description

A GPS navigation system helps users find routes between different locations. In this case study, places are represented as vertices and roads are represented as edges. Each road has a weight representing its distance.

Dijkstra's algorithm is used to find the shortest route between the starting location and the destination.

Files included:

- "GPS-Navigation-Weighted-Graph/README.md"
- "GPS-Navigation-Weighted-Graph/gps_navigation.py"

Case Study 2: ZIP/GZIP Compression Using Huffman Tree

Description

Huffman coding is a lossless data compression technique. It uses the frequency of characters to generate binary codes. Characters that appear more frequently generally receive shorter codes, while less frequent characters receive longer codes.

This case study demonstrates how to build a Huffman tree and use it to encode and decode text.

Files included:

- "Huffman-File-Compression/README.md"
- "Huffman-File-Compression/huffman_compression.py"

Technologies Used

- Programming Language: Python
- Data Structures: Weighted Graph, Priority Queue, Binary Tree
- Algorithms: Dijkstra's Algorithm and Huffman Coding

How to Run the Programs

Make sure Python 3 is installed on your computer.

GPS Navigation program:

python gps_navigation.py

Huffman Coding program:

python huffman_compression.py

Run each command from the corresponding program folder.

Conclusion

Through these case studies, I learned how graph algorithms can be used to find shortest routes and how Huffman coding can reduce the number of bits needed to represent data. These examples helped me understand the practical use of data structures and algorithms.

Note

These are educational implementations. The GPS program uses sample road distances and does not include live traffic information. The Huffman program demonstrates Huffman coding but does not create actual ZIP or GZIP archive files.
