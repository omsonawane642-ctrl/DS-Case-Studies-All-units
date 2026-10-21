# Case Study: Implementation of Stack and Queue Operations Using Linked Lists

**Student Name:** ____________________  
**Branch:** Computer Engineering  
**Subject:** Data Structures  
**Unit:** 3  
**College:** ____________________  
**Academic Year:** ____________________

## 1. Aim
To implement stack and queue operations using linked lists and understand the difference between them.

## 2. Introduction
Stack and queue are linear data structures. They are used to store and manage data, but they follow different rules. A stack follows **LIFO (Last In, First Out)**, which means the last item added is removed first. A queue follows **FIFO (First In, First Out)**, which means the first item added is removed first.

A linked list stores data in nodes. Each node contains a value and a link to another node. Unlike an array, a linked list does not need a fixed size in advance. In this case study, linked lists are used to implement both a stack and a queue.

## 3. Problem Statement
Implement the basic operations of a stack and a queue using linked lists. The program should allow the user to insert, remove, view, and display elements.

## 4. Objectives
- Understand the working of stack and queue.
- Learn how nodes are connected in a linked list.
- Implement `push`, `pop`, and `peek` for a stack.
- Implement `enqueue`, `dequeue`, and `peek` for a queue.
- Display the elements after operations.
- Compare the time complexity of the operations.

## 5. Theory

### Linked List
A linked list is made of nodes. Each node stores data and a reference to the next node. The first node is called the head. If there is no next node, its link is `None`.

### Stack
A stack allows insertion and deletion at one end, called the top.
- **Push:** Adds an element to the top.
- **Pop:** Removes the top element.
- **Peek:** Shows the top element without removing it.
- **Display:** Shows all elements from top to bottom.

Example: A stack of plates. The plate placed last on top is taken first.

### Queue
A queue inserts elements at the rear and removes them from the front.
- **Enqueue:** Adds an element at the rear.
- **Dequeue:** Removes the front element.
- **Peek:** Shows the front element without removing it.
- **Display:** Shows elements from front to rear.

Example: People standing in a line. The person who arrives first is served first.

## 6. Algorithm

### Stack operations
1. Create an empty stack with `top = None`.
2. For push, create a new node and make it the top node.
3. For pop, check whether the stack is empty. If not, remove the top node and move top to the next node.
4. For peek, show the top node's value if the stack is not empty.
5. For display, move from top through each node and print its value.

### Queue operations
1. Create an empty queue with `front = None` and `rear = None`.
2. For enqueue, create a new node. If the queue is empty, set both front and rear to it; otherwise link it after rear and update rear.
3. For dequeue, check whether the queue is empty. If not, remove the front node and move front to the next node.
4. If front becomes `None`, also set rear to `None`.
5. For peek, show the front node's value if the queue is not empty.
6. For display, move from front to rear and print each value.

## 7. Pseudocode

```text
STACK PUSH(value):
    create new node
    new node.next = top
    top = new node

STACK POP:
    if top is None:
        print "Stack is empty"
    else:
        value = top.data
        top = top.next
        return value

QUEUE ENQUEUE(value):
    create new node
    if rear is None:
        front = rear = new node
    else:
        rear.next = new node
        rear = new node

QUEUE DEQUEUE:
    if front is None:
        print "Queue is empty"
    else:
        value = front.data
        front = front.next
        if front is None:
            rear = None
        return value
```

## 8. Python Program
The file `stack_queue_linked_lists.py` contains a menu-based Python program. It implements a linked-list stack and a linked-list queue and lets the user try the operations.

## 9. Sample Test
Example stack operations:
- Push 10
- Push 20
- Push 30
- Display → `30 -> 20 -> 10`
- Pop → removes `30`
- Peek → `20`

Example queue operations:
- Enqueue 10
- Enqueue 20
- Enqueue 30
- Display → `10 -> 20 -> 30`
- Dequeue → removes `10`
- Peek → `20`

## 10. Complexity Analysis

| Operation | Stack | Queue |
|---|---|---|
| Insert | Push: `O(1)` | Enqueue: `O(1)` |
| Delete | Pop: `O(1)` | Dequeue: `O(1)` |
| Peek | `O(1)` | `O(1)` |
| Display all elements | `O(n)` | `O(n)` |

Here, `n` is the number of elements stored. These operation times assume that the stack uses a top pointer and the queue uses both front and rear pointers.

## 11. Advantages
- The list can grow or shrink as elements are added or removed.
- No fixed capacity is needed in advance.
- Insertions and deletions at the ends used by stack and queue are efficient.
- The implementation helps show how pointers/references connect nodes.

## 12. Disadvantages
- Each node needs extra memory for its link.
- Nodes are not stored next to each other like array elements may be.
- Accessing an item by position requires moving through the nodes.
- The program must handle empty-stack and empty-queue conditions.

## 13. Applications
- **Stack:** undo operations, browser history, expression evaluation, and function calls.
- **Queue:** printer jobs, customer-service lines, task scheduling, and requests waiting to be processed.

## 14. Conclusion
In this case study, stack and queue operations were implemented using linked lists. The stack follows LIFO and the queue follows FIFO. With suitable top, front, and rear references, the main insertion and deletion operations take `O(1)` time. This exercise helped demonstrate how linked lists can be used to build useful data structures.

## 15. References
1. Data Structures course notes on linked lists, stacks, and queues.
2. Standard Data Structures and Algorithms textbook.
3. Python documentation: https://docs.python.org/3/tutorial/
