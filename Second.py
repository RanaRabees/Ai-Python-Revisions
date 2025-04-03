# ------------------ Function --------------------


def table(n):
    return [f"{n} * {i} = {n * i}" for i in range(1, 11)]

num = int(input("Enter a number to generate its multiplication table: "))
print("\n".join(table(num)))

# ---------------- Lambda Function ----------------

table = lambda n: [f"{n} * {i} = {n * i}" for i in range(1, 11)]
num = int(input("Enter a number to generate its multiplication table: "))
print("\n".join(table(num)))

