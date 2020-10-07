#Printing Multiples Of 3 Using Range

def multiples(number, limit):
    if limit < number:
        print ("Enter Valid limit")
        return

    for x in range(number,limit+1,number):
        print(x)

multiples(3, 33)
