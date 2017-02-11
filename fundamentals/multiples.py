# multiples
for i in range(1,1000+1):  # use 11 for test, not 1001
    if i%2 == 1:
        print i

for i in range(5, 1000000+1): # use 101 for test, not 1000001
    if i%5 == 0:
        print i

# sums
a = [1,2,5,10,255,3]
theSum = 0
for i in range(0, len(a)):
    theSum = theSum + a[i]
print theSum

# averages
a = [1,2,5,10,255,3]
theAvg = 0
for i in range(0, len(a)):
    theAvg = theAvg + a[i]
theAvg = theAvg / len(a)
print theAvg
