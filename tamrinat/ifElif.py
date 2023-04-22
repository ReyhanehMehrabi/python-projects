num = int(input("Enter a number:\n "))
name = (input("Whats your name?\n"))
if num >= 90:
    print(f"%s grade is A,%d" % (name, num))
elif num >= 80:
    print(f"%s grade is B,%d" % (name, num))
elif num >= 70:
    print(f"%s grade is c,%d" % (name, num))
elif num >= 60:
    print(f"%s grade is d,%d" % (name, num))
else:
    print(f"%s grade is f,%d" % (name, num))
