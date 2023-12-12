import os


def basic_operations(a,b):
    result={}
    try:
        Sum=a+b
        result['addition']=Sum
        diff=a-b
        result['differecne']=diff
        div=a/b
        result['divide']=round(div,2)
        mul=a*b
        result['multiply']=mul
    except TypeError as e:
        print("oops, the value is not number")

    except ZeroDivisionError:
        print("oops, you are trying to divide by zero")

    return result

def power_operation(base,exponent,**kwargs):
    try:
        result=pow(base,exponent)
        
        if 'modulo' in kwargs:
            result%=kwargs['modulo']
    except TypeError:
        print("oops, the value is not number")

    return result


def apply_operations(operation_list):
    result=map(lambda x:x[0](*x[1]),operation_list)
    return list(result)




#when the file is created
current_file_path = os.path.realpath(__file__)
file_stat = os.stat(current_file_path)
created_time=file_stat.st_ctime
