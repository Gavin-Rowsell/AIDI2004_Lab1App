grade = float(input("Enter grade: "))

if (grade >= 50 and grade <= 100):
	print("You passed!")
elif (grade < 50 and grade >= 0):
	print("You failed!")
else:
	print("Invalid grade!")