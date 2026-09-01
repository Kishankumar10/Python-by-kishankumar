# 10. Circular Shift (Rotation)

# Practice Problem: Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.

List = [1, 2, 3, 4, 5]
Shift = 2
Direction = "right"

def rotate_list(lst, n, direction):
    n = n % len(lst)
    if direction == "right":
        return lst[-n:] + lst[:-n]
    elif direction == "left":
        return lst[n:] + lst[:n]

print(rotate_list(List, Shift, Direction))