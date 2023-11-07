def print_equilateral_triangle(height):
    for i in range(1, height + 1):
        print(" " * (height - i), end="")
        print("* " * i)
height = int(input("Enter the triangle range: "))
print_equilateral_triangle(height)
