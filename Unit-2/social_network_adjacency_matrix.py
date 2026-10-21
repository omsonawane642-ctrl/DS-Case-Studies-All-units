# Case Study: Social Network Adjacency Matrix
# Small educational example of users and friendship connections.

users = ["Asha", "Bharat", "Charu", "Dev", "Esha"]
size = len(users)

# Create a square matrix filled with zeros.
matrix = [[0 for _ in range(size)] for _ in range(size)]

# Friendship connections are undirected.
friendships = [
    ("Asha", "Bharat"),
    ("Asha", "Charu"),
    ("Bharat", "Dev"),
    ("Charu", "Esha"),
]

# Store each friendship in both directions.
for user1, user2 in friendships:
    i = users.index(user1)
    j = users.index(user2)
    matrix[i][j] = 1
    matrix[j][i] = 1

print("Social Network Adjacency Matrix")
print("       " + " ".join(f"{user:>7}" for user in users))

for i, user in enumerate(users):
    print(f"{user:<7}" + " ".join(f"{value:>7}" for value in matrix[i]))


def are_friends(user1, user2):
    """Return True if the two listed users are friends."""
    i = users.index(user1)
    j = users.index(user2)
    return matrix[i][j] == 1


print()
print("Are Asha and Bharat friends?", "Yes" if are_friends("Asha", "Bharat") else "No")
print("Are Asha and Dev friends?", "Yes" if are_friends("Asha", "Dev") else "No")
