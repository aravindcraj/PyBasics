class SwapIt:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def swap(self):
        temp = self.a
        self.a = self.b
        self.b = temp

        print "\nAfter Swapping: ";
        print "\n Value of A: ", self.a, "\n Value of B: ", self.b

a = int(raw_input("Enter a value for A: "))
b = int(raw_input("Enter a value for B: "))

print "\nBefore Swapping: "
print "\n Value of A: ", a, "\n Value of B: ", b

sw = SwapIt(a, b)
sw.swap()
