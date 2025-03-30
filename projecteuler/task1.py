import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем время начала выполнения
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        end_time = time.time()  # Засекаем время окончания выполнения
        elapsed_time = end_time - start_time  # Вычисляем время выполнения
        print(f"Функция {func.__name__} выполнилась за {elapsed_time:.4f} секунд")
        return result
    return wrapper


def sum_simple():

    sum = 0

    for x in range(1, 1000):
        if (x % 3 == 0 or x % 5 == 0):
        #    print(x)
            sum = (sum + x)

    return sum

print(sum_simple())

def sum_divisors(N, q):

    count = (N-1) // q

    sap = (count * (count + 1)) // 2

    return q * sap

def sum_sap():
    return sum_divisors(1000, 3) + sum_divisors(1000, 5) - sum_divisors(1000, 15)

@timer_decorator
def test1():
    for i in range(1, 10000):
        sum_simple()

@timer_decorator
def test2():
    for i in range(1, 10000):
        sum_sap()

test1()
test2()

# 1 2 3 4 5 ...

# 1 + 2 + 3 + ... + 99 + 100 = 50 * 101 = 5050

# n/2 (n+1) = (n * (n+1))/2 = 1 + 2 + ... + n

# 3 + 6 + 9 + 12 + 15 + ... + 999 [1000/3 чисел] N = 1000, q = 3
# 3 * (1 + 2 + 3 +... + 333) = 3 * 333 * 334 / 2 = 166833


# 5 + 10 + 15 + ... + 995 [1000/5 ]
# 5 * (1 + 2 + ... + 199) = 5 * (199 * 200) / 2 = 99500

# 15 + 30 + 45 + ... + 990
# 15 (1 + 2 + ... + 66) = 15 * 66 * 67 /2 = 33165

# 166833 + 99500 - 33165 = 222168


# 1101001000010000100000....
# s(N)