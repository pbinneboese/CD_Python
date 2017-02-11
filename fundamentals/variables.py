number = 42
print(id(number),number);
a = 'this is a string'
print(type(a),a);
b = '''\
    this String
    is indented
'''
print(b);
c = 34
d = "this string {} has an insert".format(c)
print(d);
e = [1,2,3,4,5]
print(e,"contains",e[1:2]);
DictType = dict(key1 = 2.5, key2 = 'alps', key3 = c)
print(type(DictType),DictType)
