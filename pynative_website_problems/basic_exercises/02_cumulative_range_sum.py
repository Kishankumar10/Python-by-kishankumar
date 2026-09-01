# 2. Cumulative Sum of a Range

# Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

def get_range_sum(start, end):
    pre_num = 0
    for i in range(start, end):
        print(f"Current Number {i} Previous Number {pre_num} Sum: {pre_num + i}")
        pre_num = i

get_range_sum(0,10)