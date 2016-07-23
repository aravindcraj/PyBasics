a = int(raw_input("Enter a value for A: "))

b = int(raw_input("Enter a value for B: "))
array = [10, 20, 50, 65]

if a in array:
    print "A is present in the array"

else:
    print "A is not present in the array"

if b not in array:
    print "B is not present in the array"

else:
    print "B is present in the array"

if a is b:
    print "A and B has same identity"

else:
    print "A and B doesn't have same identity"

if id(a) is id(b):
    print "A and B has same identity"

else:
    print "A and B doesn't have same identity"
