# Case Study: Social Network Adjacency Matrix
## Representing Friendship Connections Among Millions of Users

**Student Name:** ____________________  
**Class / Branch:** Computer Engineering  
**Subject:** Data Structures  
**Unit:** ____________________  
**College:** ____________________  
**Academic Year:** ____________________

## 1. Introduction
Social networking applications allow users to connect with friends. In graph theory, each user can be represented as a **vertex (node)**, and each friendship can be represented as an **edge**. A data structure is needed to store these connections so the application can check whether two users are friends and explore connections between users.

An **adjacency matrix** is a square table used to represent a graph. If there are `V` users, the matrix has `V` rows and `V` columns. The entry `matrix[i][j]` is `1` when user `i` and user `j` are friends; otherwise it is `0`.

## 2. Problem Statement
Design a simple model that represents friendship connections in a social network using an adjacency matrix. Demonstrate adding friendship connections and checking whether two users are friends. Discuss whether this representation is suitable for millions of users.

## 3. Objectives
- Understand how a graph represents users and friendships.
- Build an adjacency matrix for a small sample network.
- Add undirected friendship connections.
- Check whether two users are friends.
- Analyze the time and space complexity.
- Explain the limitations of using a matrix at very large scale.

## 4. Theory
### Graph
A graph consists of vertices and edges. In this example, each vertex is a user and each edge is a friendship.

### Adjacency Matrix
For `V` users, an adjacency matrix contains `V × V` entries:
- `1` means a friendship exists.
- `0` means no friendship is recorded.
- For an undirected friendship graph, the matrix is symmetric: if A is friends with B, both `matrix[A][B]` and `matrix[B][A]` are `1`.
- The diagonal is usually `0` when a user is not considered their own friend.

## 5. Example
Consider five users: Asha, Bharat, Charu, Dev, and Esha. Suppose:
- Asha is friends with Bharat and Charu.
- Bharat is friends with Dev.
- Charu is friends with Esha.

The adjacency matrix is:

| User | Asha | Bharat | Charu | Dev | Esha |
|---|---:|---:|---:|---:|---:|
| **Asha** | 0 | 1 | 1 | 0 | 0 |
| **Bharat** | 1 | 0 | 0 | 1 | 0 |
| **Charu** | 1 | 0 | 0 | 0 | 1 |
| **Dev** | 0 | 1 | 0 | 0 | 0 |
| **Esha** | 0 | 0 | 1 | 0 | 0 |

For example, the value in row Asha and column Bharat is `1`, so Asha and Bharat are friends.

## 6. Algorithm
1. Create a list of user names.
2. Create a square matrix filled with zeros.
3. For each friendship pair `(u, v)`, set both `matrix[u][v]` and `matrix[v][u]` to `1`.
4. To check whether two users are friends, inspect the corresponding matrix entry.
5. Display the matrix and the result of a sample friendship check.

## 7. Pseudocode
```text
START
  Read list of users
  Create V × V matrix filled with 0
  FOR each friendship (u, v)
      matrix[u][v] = 1
      matrix[v][u] = 1
  END FOR
  Display matrix
  Check matrix[index_of_user1][index_of_user2]
  If value is 1, print "They are friends"
  Otherwise, print "They are not friends"
END
```

## 8. Python Implementation
The included `social_network_adjacency_matrix.py` file implements the five-user example.

## 9. Sample Output
```text
Social Network Adjacency Matrix
           Asha  Bharat  Charu     Dev    Esha
Asha          0       1      1       0       0
Bharat        1       0      0       1       0
Charu         1       0      0       0       1
Dev           0       1      0       0       0
Esha          0       0      1       0       0

Are Asha and Bharat friends? Yes
Are Asha and Dev friends? No
```

## 10. Complexity Analysis
Let `V` be the number of users and `E` be the number of friendship connections.

- **Space complexity:** `O(V²)` because the matrix stores an entry for every possible pair of users.
- **Check friendship:** `O(1)` because one matrix cell is accessed.
- **Add a friendship:** `O(1)` when the matrix already exists, because two entries are updated.
- **Initialize the matrix:** `O(V²)` time and space.

### Is it practical for millions of users?
Usually not. With one million users, the matrix contains `1,000,000 × 1,000,000 = 1,000,000,000,000` entries (one trillion). Even if each entry used only one byte, this would require roughly **1 terabyte** of memory (about 0.91 TiB), ignoring overhead. A typical Python list-of-lists matrix would use far more memory.

A real social network is generally sparse: each user is connected to a tiny fraction of all possible users. An adjacency list stores only actual connections and typically uses `O(V + E)` space, so it is usually a better choice for large sparse networks. A matrix is still useful for learning and for small or dense graphs.

## 11. Advantages
- Simple to understand and implement.
- Fast `O(1)` friendship lookup.
- Useful for small networks or dense graphs.
- Makes the graph's connections easy to display in a table.

## 12. Disadvantages
- Requires `O(V²)` memory even when very few friendships exist.
- Initializing the matrix is expensive for large graphs.
- Adding users can require resizing or rebuilding the matrix.
- Not suitable for millions of users in ordinary in-memory form.

## 13. Applications
- Demonstrating graph representation in data structures.
- Small friendship networks and classroom examples.
- Dense graphs where many pairs are connected.
- Comparing matrix representation with adjacency lists.

## 14. Conclusion
An adjacency matrix is a clear way to represent friendship connections and makes checking a connection very fast. However, its memory requirement grows quadratically with the number of users. Therefore, although it is suitable for a small demonstration, it is not a practical standalone representation for a social network containing millions of users. Sparse representations such as adjacency lists are generally more memory-efficient for large social networks.

## 15. References
1. Course notes on Graphs and Graph Representations.
2. Standard Data Structures and Algorithms textbooks, graph representation chapter.
3. Python documentation: https://docs.python.org/3/tutorial/
