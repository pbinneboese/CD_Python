# the random function will return a floating point number,
# that is 0.0 <= random_num < 1.0
import random
#random_num = random.random()
#
def headOrTail():   # returns True if heads, False if tails
    result = round(random.random())
    # print result
    if result == 1:
        return True
    else:
        return False
#
def tossTheCoin(numTimes):
    heads = 0
    tails = 0
    for i in range(0,numTimes):
        str = "Attempt #{}: Throwing a coin... It's a ".format(i)
        if headOrTail():
            heads += 1
            str += "head!"
        else:
            tails += 1
            str += "tail!"
        str += " ... Got {} head(s) so far and {} tail(s) so far".format(heads,tails)
        print str
    return
#
print "Starting the program..."
tossTheCoin(5000) # use 10 for test instead of 5000
print "Ending the program, thank you!"
#
