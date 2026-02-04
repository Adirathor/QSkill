import numpy as np
def input_matrix(name):
    r = int(input(f"Enter rows for {name}: "))
    c = int(input(f"Enter columns for {name}: "))
    print(f"Enter elements for {name}:")
    mat = []
    for i in range(r):
        row = list(map(float, input().split()))
        mat.append(row)
    return np.array(mat)
A = input_matrix("Matrix A")
B = input_matrix("Matrix B")
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
while True:
    print("\nChoose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result:\n", A + B)
    elif choice == 2:
        print("Result:\n", A - B)
    elif choice == 3:
        print("Result:\n", np.dot(A, B))
    elif choice == 4:
        print("Transpose of A:\n", A.T)
        print("Transpose of B:\n", B.T)
    elif choice == 5:
        if A.shape[0] == A.shape[1]:
            print("Determinant of A:", np.linalg.det(A))
        else:
            print("Matrix A is not square.")
    elif choice == 6:
        break
    else:
        print("Invalid choice")