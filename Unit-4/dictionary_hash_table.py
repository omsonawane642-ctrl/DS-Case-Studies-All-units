# Unit 4 Case Study: Dictionary Using a Hash Table
# Collision resolution method: separate chaining.

class DictionaryHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, word):
        # Simple educational hash function.
        return sum(ord(char) for char in word.lower()) % self.size

    def add_or_update(self, word, meaning):
        word = word.strip().lower()
        meaning = meaning.strip()

        if not word:
            print("Word cannot be empty.")
            return
        if not meaning:
            print("Meaning cannot be empty.")
            return

        index = self._hash(word)
        chain = self.table[index]

        for position, (stored_word, _) in enumerate(chain):
            if stored_word == word:
                chain[position] = (word, meaning)
                print("Meaning updated.")
                return

        chain.append((word, meaning))
        print(f"Word added at table index {index}.")

    def search(self, word):
        word = word.strip().lower()
        index = self._hash(word)

        for stored_word, meaning in self.table[index]:
            if stored_word == word:
                return meaning
        return None

    def display(self):
        found = False
        print("\nDictionary entries:")
        for index, chain in enumerate(self.table):
            if chain:
                found = True
                entries = ", ".join(f"{word}: {meaning}" for word, meaning in chain)
                print(f"Index {index}: {entries}")
        if not found:
            print("Dictionary is empty.")


def main():
    dictionary = DictionaryHashTable()

    while True:
        print("\nDICTIONARY MENU")
        print("1. Add a word or update its meaning")
        print("2. Search for a word")
        print("3. Display all words")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            word = input("Enter word: ")
            meaning = input("Enter meaning: ")
            dictionary.add_or_update(word, meaning)
        elif choice == "2":
            word = input("Enter word to search: ")
            meaning = dictionary.search(word)
            if meaning is None:
                print("Word not found.")
            else:
                print(f"Meaning of {word.strip().lower()}: {meaning}")
        elif choice == "3":
            dictionary.display()
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
