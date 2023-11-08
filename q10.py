import random
import sys

def get_random_int(a, b):
    return random.randint(a, b)

a = int(sys.argv[1])
b = int(sys.argv[2])

if a > b:
    print("Error: a should be less than or equal to b")
    sys.exit(1)

random_int = get_random_int(a, b)
print(f"Random integer between {a} and {b}: {random_int}")