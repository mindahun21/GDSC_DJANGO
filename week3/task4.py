# Write a Python program to find and print the sum of all the even numbers from 1 to 50 (inclusive). Additionally, for each even number, if it is a multiple of 3, print "Three" instead of the number; if it is a multiple of 5, print "Five" instead of the number. Finally, print the total sum and the count of numbers replaced with "Three" or "Five."

sumOfEven=0
count=0
sumOfReplaced=0
for i in range(1,51):
    if i%2==0:
        sumOfEven+=i
        if i%3==0:
            print("Three",end=" ")
            sumOfReplaced+=i
            count+=1
        elif i%5==0:
            print("Five",end=" ")
            sumOfReplaced+=i
            count+=1
        else:
            print(i,end=" ")
    else:
        print(i,end=" ")





print(f"the sum of all the even numbers from 1 to 50 (inclusive) is {sumOfEven}")
print(f"the count of numbers replaced with 'Three' or 'Five' is {count}")
print(f"the sum of all the numbers replaced with 'Three' or 'Five' is {sumOfReplaced}")