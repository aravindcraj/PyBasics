num = int(raw_input("Enter a sequence of numbers to reverse: "))

rev = 0

while num != 0:
    rev *= 10
    rev += num % 10
    num /= 10

print "Reverse number is: ", rev
