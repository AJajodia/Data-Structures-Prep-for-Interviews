import random
randlist = [random.randint(0, 100) for i in range(10)]
print(randlist)


# Write a function with O(n^2) to find min number
def square(numbers):
    smallest = (0, 0)
    for i in numbers:
        correct_count = 0
        for j in numbers:
            if j >= i:
                correct_count += 1
            if correct_count > smallest[1]:
                smallest = (i, correct_count)

    return smallest[0]


# write a function with O(n) to find min number
def linear(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i <= smallest:
            smallest = i
    return smallest


print("Square result: " + str(square(randlist)))
print("Linear result: " + str(linear(randlist)))
