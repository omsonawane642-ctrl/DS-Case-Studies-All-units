# Unit 3 Case Study: Stack and Queue Using Linked Lists
# Simple menu-based implementation for learning and practice.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        print("Top -> ", end="")
        while current:
            print(current.data, end="")
            current = current.next
            if current:
                print(" -> ", end="")
        print()


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        print("Front -> ", end="")
        while current:
            print(current.data, end="")
            current = current.next
            if current:
                print(" -> ", end="")
        print(" <- Rear")


def stack_menu(stack):
    while True:
        print("\nStack Menu: 1.Push  2.Pop  3.Peek  4.Display  0.Back")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            value = input("Enter value: ")
            stack.push(value)
            print("Value pushed.")
        elif choice == "2":
            value = stack.pop()
            if value is not None:
                print("Popped:", value)
        elif choice == "3":
            value = stack.peek()
            if value is not None:
                print("Top value:", value)
        elif choice == "4":
            stack.display()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


def queue_menu(queue):
    while True:
        print("\nQueue Menu: 1.Enqueue  2.Dequeue  3.Peek  4.Display  0.Back")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            value = input("Enter value: ")
            queue.enqueue(value)
            print("Value added.")
        elif choice == "2":
            value = queue.dequeue()
            if value is not None:
                print("Dequeued:", value)
        elif choice == "3":
            value = queue.peek()
            if value is not None:
                print("Front value:", value)
        elif choice == "4":
            queue.display()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


def main():
    stack = LinkedStack()
    queue = LinkedQueue()

    while True:
        print("\nMAIN MENU")
        print("1. Stack operations")
        print("2. Queue operations")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            stack_menu(stack)
        elif choice == "2":
            queue_menu(queue)
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
