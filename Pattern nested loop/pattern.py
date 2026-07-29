# hollow square pattern
# size = 5
# for i in range(size):
#     for j in range(size):
#         # print * completely in first and last row
#         # print * only in first and last position in other rows
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()

# pyramid star pattern
# n = 5
# for i in range(n):
#     for j in range(n-1 , -1 ,-1):
#         print(' ', end='')
#     for k in range(2 * i + 1):
#         print('*', end='')
#     print()


    # Box_pattern

# n = int(input("Enter a number : "))
# for i in range(n) :
#     print("* "*n)
#_________________________________________#

# right triangle pattern 

# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     print("* "*i)
#_________________________________________#

# inverse triangle 

# n = int(input("Enter a number : "))
# for i in range(n,0,-1):
#     print("* "*i)
 #_________________________________________#

rows = int(input("how many rows of time glass you want : "))  

for i in range(rows, 0, -1):  
    for j in range(rows - i):   # Print spaces for alignment
        print(" ", end=" ")  
    for k in range(2 * i - 1):  # Print stars
        print("*", end=" ")  
    print()                     # Move to the next line

for i in range(2, rows + 1):  
    for j in range(rows - i):  # Print spaces for alignment
        print(" ", end=" ")  
    for k in range(2 * i - 1):  # Print stars
        print("*", end=" ")
    print()  # Move to the next line 



