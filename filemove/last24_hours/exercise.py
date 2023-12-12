# test = lambda x:[pow(i,2) for i in x] 


# data=[1,2,3,4,5,6,]
# print(test(data))

# lambda
# higher order function
    # reduce
    # filter
    # map
    # zip
    # enumerate
    # reversed
    # set

# exption handling

# def greet(name):
#     print(f"hey {name}")


# greet("John")

# print("\n\n ========================")

# def add_numbers(num1,num2):
#     return num1 + num2


# print(add_numbers(10,20))
# print("\n\n ======================")


# def print_args(*args):
#     for arg in args:
#         print(arg,end=" ")


# print_args(1,2,3,4,5,6,7,8,9,10)

# print("\n\n ======================")


# def calculate_average(*args):
#     return sum(args)/len(args)


# print(calculate_average(1,2,3,4,5,6,7,8,9,10))
# print("\n\n ====================")


# add=lambda x,y:x+y

# print(add(12,12))


# print("\n\n ===================")

# test = lambda x:[pow(i,2) for i in x] 


# data=[1,2,3,4,5,6,]
# print(test(data))

# print("\n\n ===================")

# check_parity=lambda x:x%2==0

# print(check_parity(23))
# print("\n\n ===================")


# # filter functions

# # Example: Filtering even numbers from a list.

# def filter_even(lst):
#     return list(filter(lambda x:x%2==0,lst))

# print(filter_even([1,2,3,4,5,6,7,8,9,10]))


# print("\n\n ===================")

# # map function
# # Example: Double each number in a list.

# def map_double(lst):
#     return list(map(lambda x:x*2,lst))

# double_outPut=map_double([1,2,3,4,5,6,7,8,9,10])
# for i in double_outPut:
#     print(i,end=" ")

# print(i for i in double_outPut)


# print("\n\n ===================")

# # try and catch
# # Example: take two numbers from the user and return the sum(validate user input)

# def sum_two_numbers(num1,num2):
#     try:
#         return int(num1)+int(num2)
#     except ValueError:
#         print("Invalid input")

# print(sum_two_numbers(12,78))

# # Example: take two numbers from the users and divide the first number with the second one(try and catch division by zero error)
# print("\n\n ===================")

# def divide_two_numbers(num1,num2):
#     try:
#         return int(num1)/int(num2)
#     except ValueError:
#         print("Invalid input not number")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     finally:
#         print("done")

# print(divide_two_numbers(12,0))

# import functools


# lis=[1,2,3,4,5,6,7]
# reduced=functools.reduce(lambda a,b:a+b,lis)
# print(reduced)

# num1=[1,2,3]
# num2=[4,5,6]

# result=map(lambda x,y:x+y,num1,num2)
# print(*(i for i in result))


# ######################file handling##################

with open('file.txt','w+') as myFile:
    myFile.write("my name is mindahun debebe\ni am software developer\n")
    myFile.seek(0)
    str=myFile.read(20)
    print(str)

with open('file.txt','r') as myFile:
    for line in myFile:
        line.strip()
        print(line)