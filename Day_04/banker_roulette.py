friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
# 1st option: longest way
random_number = random.randint(0, 4)
if random_number == 0:
    print("Alice")
elif random_number == 1:
    print("Bob")
elif random_number == 2:
    print("Charlie")
elif random_number == 3:
    print("David")
else:
    print("Emanuel")

# 2nd option: better
random_number = random.randint(0, 4)
print(friends[random_number])

# 3rd option: best
print(random.choice(friends))


