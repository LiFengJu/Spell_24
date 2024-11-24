def render(n):
    operations = 0

T = int(input())

for i in range(T):
    n = int(input())
    print(render(n))


def min_operations_to_color(n, a):
    operations = 0
    while any(color == 0 for color in a):
        for i in range(n):
            if a[i] == 0:
                a[i] = 1  # Color the element
                operations += 1
                break
        # Check if the entire array is colored
        if all(color == 1 for color in a):
            break
    return operations

# Example usage
n = int(input())
a = [0] * n  # Initial array with all elements uncolored
print(min_operations_to_color(n, a))