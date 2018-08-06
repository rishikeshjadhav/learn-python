a1 = raw_input("Enter length of side a: ")
b1 = raw_input("Enter length of side b: ")
c1 = raw_input("Enter length of side c: ")

a = int(a1)
b = int(b1)
c = int(c1)

if a !=b and b != c and a !=c:
	print("Scalene")
elif a==b and b==c:
	print("equilateral")
else:
	print("Isocsles")
