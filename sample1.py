"""
num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")"""
"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
try:    
if num.isnumeric() ==False:
    raise("number is not number")
elif num2.isnumeric() ==False:
    raise("number2 is not number")
else       
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}.")"""
"""
try:
    number = float(input("Enter a number: "))

    if number > 100:
        raise ValueError("Error: Number is greater than 100.")
    else:
        print(f"{number} is within the acceptable range.")

except ValueError as e:
    print(f"Exception caught: {e}")"""
"""
num = float(input("Enter a number: "))


if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")"""
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


print(f"The largest number is: {largest}")"""
"""
try:
    # Prompt user for input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    # Compare and find the largest
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    print(f"The largest number is: {largest}")

except ValueError:
    print("Error: Please enter numeric values only.")
except TypeError:
    print("Type Error: Invalid operation with incompatible data types.")"""

"""
try:
    
    action = input("Enter action (add, sub, mul, div): ").lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    
    if action == "add":
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif action == "sub":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif action == "mul":
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif action == "div":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Invalid action. Please enter add, sub, mul, or div.")

except ValueError:
    print("Error: Please enter valid numeric inputs.")
except ZeroDivisionError as e:
    print(f"Error: {e}")"""

"""
def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


input_string = "aabcddd"
result = count_characters(input_string)


for char, count in result.items():
    print(f"'{char}': {count}")""" 

"""
    char_count=();
    name="hi how are you"
    for(c in name):
        if not c in char_count:
            char_count[c]=0
            else:
                char_count[c]+=1
                print(char_count)"""

char_count = {}  
name = "hi how are you"

for c in name:
    if c not in char_count:
        char_count[c] = 1
    else:
        char_count[c] += 1  

print(char_count)                  