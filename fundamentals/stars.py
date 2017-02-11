# stars, part 1
#
def convertToChars(num, chr): # return string with num characters of chr
    str = ""
    for i in range(0,num):
        str += chr
    return str
#
def draw_stars(arr, chr):
    for i in arr:
        str1 = convertToChars(i, chr)
        print (str1)
    return
#
starArray = [4,6,1,3,5,7,25]
print "stars part 1"
draw_stars(starArray,"*")
#
# stars, part 2
def draw_stars2(wordList):
    for i in wordList:
        if type(i) is int:
            chr = "*"
            num = i
        elif type(i) is str:
            chr = i[0].lower()
            num = len(i)
        # print chr, num
        str1 = convertToChars(num, chr)
        print (str1)
        # draw_stars(starArray,chr)
    return
#
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print "stars part 2"
draw_stars2(x)
