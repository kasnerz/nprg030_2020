import random

random.seed(42)

def is_sorted(l):
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True


def bogosort(l):
    print("Sorting...")
    step = 0

    while not is_sorted(l):
        print(f"step #{step}: {l}")
        random.shuffle(l)
        step += 1

    return l


l = [5, 1, 2, 4, 3]

l_sorted = bogosort(l)

print("\nSorted array:")
print(l_sorted)