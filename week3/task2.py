
#2. Write a program that prints the following pattern.
    # The program should accept the input for character
    # The pattern consists of a series of lines
    # The characters in each line should follow a specific pattern based on the line number.
    # Use conditional statements to determine the pattern for each line.
    # Use a loop to iterate through the lines and print the characters accordingly.
    # You are not allowed to use functions in your code.
    # Do not store the pattern or any intermediate results in variables.


character=input("plase enter the pattern to be printed: ")
if len(character)>1:
    print("the length of the character should be 1")
elif character.lower() in ['a','e','i','o','u']:
    print("vowels are not allowed in the input")
else:
    for i in range(5):
        for j in range((i+1)+i):
            print(character,end="")
        print()
