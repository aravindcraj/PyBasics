print "Arithmetic operations using switch operator"
a = int(input("Enter a value for A: "))
b = int(input("Enter a value for B: "))

choice = int(input(
    "Enter your choice of arithmetic operation you want to perform \n \t 1. Add \n \t 2. Sub \n \t 3. Multiply \n \t 4. Division \n \t 5. Modulus \n \t 6. Exponent \n \t 7. Floor Division"))

if choice == 1:

    c = a + b
    print "Sum is: ", c

elif choice == 2:

    c = a - b
    print "Difference is: ", c

elif choice == 3:

    c = a * b
    print "Product is: ", c

elif choice == 4:

    c = a / b
    print "Quotient is: ", c

elif choice == 5:

    c = a % b
    print "Modulus is: ", c

elif choice == 6:

    c = a**b
    print "Exponent is: ", c

elif choice == 7:

    c = a//b
    print "Floor division value is: ", c

else:
    print "Invalid choice, Try again"
