# 3. Develop a program that checks if a user-inputted word is a palindrome. A palindrome is a word that reads the same backward as forward (e.g., "radar").


word=input("plase enter the word to be checked: ")
if word==word[::-1]:
    print(f"the word {word} is a palindrome")
else:
    print(f"the word {word} is not a palendrome \n because {word[::-1]} is not equl to {word}")