'''
print("Please enter your age: ")
try:
    age = int(input())
    print(f"you are {age} years old")
except:
    print("You entered an invalid value")
'''

print("Welcome to the times table quiz")
print("Enter a times table that you would like to be tested on:")

times_table = int(input())


print("Enter the maximum value for your times table: ")
try:
    max_value = int(input())
    max_value = max_value + 1
    answer = 0
    print(f"Here is your quiz on the {times_table} times table")
    for x in range(1, max_value):
        answer = x * times_table
        print(f"{x} times {times_table} is ...")
        print("Answer:")
        user_answer = int(input())
        if user_answer == answer:
            print("Correct")
        else:
            print("Incorrect")
except:
    print("value is not accepted")

 