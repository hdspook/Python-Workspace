#Summing Values using multiple arguments

def addition(*args):
    result = 0

    for x in args:
        result += x

    return result

print(addition(2,3,4,5))
