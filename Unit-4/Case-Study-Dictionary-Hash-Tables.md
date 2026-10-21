# Case Study: Dictionary Application Using Hash Tables
## Storing and Retrieving Words and Meanings with Collision Resolution

**Student Name:** ____________________  
**Branch:** Computer Engineering  
**Subject:** Data Structures  
**Unit:** 4  
**College:** ____________________  
**Academic Year:** ____________________

## 1. Aim
To implement a dictionary application that stores and retrieves words and their meanings using a hash table and handles collisions.

## 2. Introduction
A dictionary stores words with their meanings. When we search for a word, we want to find its meaning quickly. A hash table is one data structure that can help with this.

A hash table uses a **hash function** to convert a key, such as a word, into an index in an array. The word and its meaning are stored at that index. Sometimes two different words can produce the same index. This is called a **collision**. In this case study, collisions are handled using **separate chaining**, where each table position contains a list of word-meaning pairs.

## 3. Problem Statement
Create a simple dictionary program in which a user can add words with meanings, search for a word, update its meaning, and display the stored entries. The program should handle cases where different words map to the same table index.

## 4. Objectives
- Understand the basic working of a hash table.
- Use a word as the key and its meaning as the value.
- Apply a hash function to calculate an index.
- Handle collisions using separate chaining.
- Implement insertion, search, update, and display operations.
- Study the time and space complexity.

## 5. Theory

### Hash Table
A hash table stores key-value pairs. In this program, the key is the word and the value is its meaning. The hash function maps a word to an index in the table.

### Hash Function
The example uses a simple hash function that adds the Unicode values of the letters and takes the remainder after division by the table size. This makes an index within the table. This function is easy to understand for a classroom example, but it is not a secure or especially strong hash function.

### Collision
A collision happens when two different words produce the same index. For example, with this simple function, some different words may have the same sum of character values.

### Collision Resolution: Separate Chaining
Each table index stores a list (chain). If several words map to the same index, their word-meaning pairs are stored in that list. When searching, the program calculates the index and checks the entries in that chain.

## 6. Algorithm
### Add or Update a Word
1. Read a word and its meaning.
2. Convert the word to lowercase so searches are not affected by letter case.
3. Calculate the index using the hash function.
4. Check the chain at that index.
5. If the word is already present, update its meaning.
6. Otherwise, add the word and meaning to the chain.

### Search for a Word
1. Read the word to search for.
2. Convert it to lowercase.
3. Calculate its hash index.
4. Search the chain at that index.
5. If the word is found, display its meaning; otherwise, display a message that it was not found.

## 7. Pseudocode
```text
HASH(word):
    total = sum of character codes in word
    return total modulo table_size

ADD(word, meaning):
    index = HASH(word)
    for each entry in table[index]:
        if entry.word equals word:
            update entry.meaning
            return
    append (word, meaning) to table[index]

SEARCH(word):
    index = HASH(word)
    for each entry in table[index]:
        if entry.word equals word:
            return entry.meaning
    return NOT_FOUND
```

## 8. Python Program
The file `dictionary_hash_table.py` contains a menu-based implementation with options to add a word, search for a word, display all entries, and exit. It uses separate chaining to resolve collisions.

## 9. Sample Example
Suppose the user adds:
- `apple` — a fruit
- `book` — a set of pages joined together
- `computer` — an electronic device used to process data

The user can then search for `apple` and the program displays its meaning. If two words map to the same index, both are kept in the same chain, so neither entry is lost.

## 10. Complexity Analysis
Let `n` be the number of stored words and `m` be the number of table slots.

- **Insert:** Average `O(1)` when words are spread across the table; worst case `O(n)` if many entries fall into one chain.
- **Search:** Average `O(1)` with a good distribution; worst case `O(n)`.
- **Update:** Average `O(1)`; worst case `O(n)`.
- **Display all entries:** `O(n + m)` because the program checks each table slot and each stored entry.
- **Space complexity:** `O(n + m)` for the table and stored entries.

The performance depends on the hash function and how evenly it distributes words.

## 11. Advantages
- Usually allows quick word lookup.
- Stores each word with its meaning as a key-value pair.
- Separate chaining can handle multiple words at the same index.
- The program can update a meaning without adding a duplicate word.

## 12. Disadvantages
- Different words can have the same hash index.
- A weak hash function can create long chains and slower searches.
- The basic program stores data only while it is running; it does not save entries to a file.
- A hash table does not automatically display words in alphabetical order.

## 13. Applications
- Simple dictionaries and glossaries.
- Contact lookup by name.
- Caches and symbol tables.
- Storing and retrieving records using keys.

## 14. Conclusion
In this case study, a small dictionary was implemented using a hash table. The hash function selects a table index for each word, and separate chaining handles collisions by storing multiple entries in one chain. This approach usually makes searching quick, although performance depends on the hash function and the number of collisions.

## 15. References
1. Data Structures course notes on hashing and hash tables.
2. Standard Data Structures and Algorithms textbook, hashing chapter.
3. Python documentation: https://docs.python.org/3/tutorial/
