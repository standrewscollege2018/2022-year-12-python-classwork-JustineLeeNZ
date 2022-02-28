''' demo of a function '''


def to_the_power(a, b):
    answer = a**b

print("Enter a number:")
num1 = int(input())
print("Enter a second number:")
num2 = int(input())

to_the_power(num1, num2)

print(f"{num1} to the power of {num2} is {answer}")
