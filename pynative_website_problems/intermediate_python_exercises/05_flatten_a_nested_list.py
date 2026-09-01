#  5. Flatten a Nested List

# Practice Problem: Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.


# version - 1 : (the result is outside function and it is a shared state so that, it is a major weakness as the function is not reusable)

nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = []

def flatter(nested):
    if type(nested) == int:
        result.append(nested)
        return None
    for items in nested:
        flatter(items)

flatter(nested_list)
print(result)   


# version - 2 : (using extend)

nested_list = [1, [2, 3], [4, [5, 6]], 7]


def flatten(nested):
    if not isinstance(nested, list):  
        return [nested]
    flat = []
    for items in nested:
        flat.extend(flatten(items))
    return flat

print(flatten(nested_list))


# more elegant flow version 

nested_list = [1, [2, 3], [4, [5, 6]], 7]

def flatten(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

print(flatten(nested_list))