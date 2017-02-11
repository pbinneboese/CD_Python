# find & replace
str = "If monkeys like bananas, then I must be a monkey!"
sub = "monkey"
x = str.count(sub)
print sub,"found ",x,"times"
str2 = str.replace(sub, "alligator")
print str2

# min & max
x = [2,54,-2,7,12,98]
minX = min(x)
maxX = max(x)
print "min=",minX,"max=",maxX

# first & last
x = ["hello",2,54,-2,7,12,98,"world"]
firstX = x[0]
lastX = x[len(x)-1]
print "first=",firstX,"last=",lastX
y = [firstX,lastX]
print y

#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[0:2]
x.pop(0)
x.pop(0)
x.insert(0,y)
print x
