import random
from collections import Counter,deque
import math

# random module

for i in range(20):
    print(random.random())

for i in range(20):
    print(random.randint(1,10))

for i in range(20):
    print(random.randrange(1,5))

for i in range(20):
    print(random.uniform(1,3))  

my_list = ["aaa","bbb","ccc","ddd"]

for i in range(20):
    print(random.choice(my_list))

for i in range(20):
    print(random.choices(my_list,k=2))

for i in range(20):
    print(random.sample(my_list,k=2))

random.shuffle(my_list)
print(my_list)

# collection module

my_numbers = [1,2,3,5,6,4,2,1,3,6,2,1,4,5,3,6]
print(Counter(my_numbers))


d = deque([1, 2, 3])

d.append("right")
d.appendleft("left")

print(d,"before pop")

right = d.pop()
print(d)
left = d.popleft()
print(d)

# experiments

# print(math.__dict__.keys())
# help(math)


# a = 0
# while True:      
#     a = float(input("Test number : "))
#     print(f"Result : {math.trunc(a)}","\n")

# math module

print(math.sqrt(225))
print(math.pi)
print(math.ceil(12.56))
print(math.ceil(-12.56))
print(math.floor(12.56))
print(math.floor(-12.56))
print(math.trunc(12.56))
print(math.trunc(-12.56))
print(math.fabs(-12.56))