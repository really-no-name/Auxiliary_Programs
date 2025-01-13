def toggle(matrix, x, y, n):
    """Toggle the value of matrix[x][y] and its neighbors."""
    positions = [(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for i, j in positions:
        if 0 <= i < n and 0 <= j < n:
            matrix[i][j] = 1 - matrix[i][j]

def is_all_ones(matrix):
    """Check if all elements in the matrix are 1."""
    for row in matrix:
        if any(val == 0 for val in row):
            return False
    return True

def print_matrix(matrix):
    """Print the matrix."""
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

# Input matrix dimensions
n = int(input("Enter the dimension of the matrix (n x n): "))

# Initialize matrix
matrix = []
print(f"Enter the initial {n}x{n} matrix values (0 or 1):")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Print the initial matrix
print("Initial Matrix:")
print_matrix(matrix)

operations = []

# Perform operations until the matrix is all ones
while not is_all_ones(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                toggle(matrix, i, j, n)
                operations.append((i, j))
                print(f"After toggling ({i}, {j}):")
                print_matrix(matrix)
                if is_all_ones(matrix):
                    break
        if is_all_ones(matrix):
            break

# Print the sequence of operations
print("Sequence of operations to make all elements 1:")
for op in operations:
    print(f"Toggle at position {op}")
