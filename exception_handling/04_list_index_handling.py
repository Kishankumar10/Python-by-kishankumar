# 4. List Index Handling

# Question : Given a list of numbers, ask the user for an index and display the corresponding element. Handle IndexError.

my_list = [10, 20, 30, 40, 50]

index = int(input("Enter a index position to get printed : "))

try:
    extracted_item = my_list[index]
except IndexError:
    print("Error: Index is out of range.")
else :
    print(extracted_item)