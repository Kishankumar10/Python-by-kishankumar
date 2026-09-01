# 11: Dictionary Merging (Value Grouping)

# Practice Problem: Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.

# version - 1:

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

def group_dict_values(d1, d2):
    result = {}
    for key,value in d1.items():
        result[key] = [value]
    for key,value in d2.items():
        if key in result:
            result[key].append(value)
        else :
            result[key] = [value]
    return result

print(group_dict_values(dict_1, dict_2))

# version - 2 :

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

def group_dict_values(d1, d2):
    result = {}
    for key,value in d1.items():
        result[key] = [value]
    for key,value in d2.items():
        result[key] = result.get(key, []) + [value]
    return result

print(group_dict_values(dict_1, dict_2))