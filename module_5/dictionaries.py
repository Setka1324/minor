# Exercise 1
my_class = {
    "Ralph": 4,
    "Diana": 8,
    "Jordi": 7,
    "Michele": 5
}

# Exercise 2
my_class["Gretel"] = 9

# Print to verify that Gretel has been added
print(my_class)

# Exercise 3
name = input("Enter a name: ")

if name in my_class:
    print(f"{name} is a student in this class, and has the grade: {my_class[name]}.")
else:
    print(f"{name} is not a student in this class.")

# Exercise 4
students = ["Michele", "Diana", "Maria", "Ralph", "Jacobus"]

for student in students:
    grade = my_class.get(student, "n/a")
    print(f"{student}: {grade}")
