# odd/even
def oddEven():
    # for i in range(1,2000+1):  # use 11 for test, not 2001
    for i in range(1,10+1):  # use 11 for test, not 2001
        if i%2 == 1:
            print "Number is",i, ". This is an odd number"
        else:
            print "Number is",i, ". This is an odd number"
    return
#
oddEven()

# multiply
def multiply(listIn,multiplier):
    for i in range(0, len(listIn)):
        listIn[i] *= multiplier
    return listIn
#
a = [2,4,10,16]
a = multiply(a,5)
print a

# hacker challenge
def layered_multiples(arr):
    arrB = []
    for i in range(0, len(arr)):
        arrC = []
        for j in range(0, arr[i]+1):
            arrC.append(1)
        arrB.append(arrC)
        # print arrB[i]
    return arrB
#
# y = multiply([2,4,5],3)
# print y
x = layered_multiples(multiply([2,4,5],3))
print x
