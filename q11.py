import random

def dice():
    sum=0
    a=random.randint(1,6)
    b=random.randint(1,6)
    sum=a+b
    return sum

    
def main():
    store=dice()
    print("print sum:" {store})