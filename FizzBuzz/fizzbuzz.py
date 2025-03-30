import math

# print("123")

def remainder(aaaaablabla, b):
    r = math.floor(aaaaablabla/b)
    q = r*b

    return aaaaablabla-q


N = 100;

# print(remainder(60, 5))

for i in range(1, N + 1):
    # if (remainder(i, 3) == 0 and remainder(i, 5) == 0):
    # if (remainder(i, 3 * 5) == 0):
    if ((i % (3 * 5)) == 0):
        print("FizzBuzz")
    elif ((i % 5) == 0):
        print("Buzz")
    elif (remainder(i, 3) == 0):
        print("Fizz")
    else:
        print(i)
