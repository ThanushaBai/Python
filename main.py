#tuple

student = ("t",21,"female")

print(student.count("female"))
print(student.index("female"))

for x in student:
    print(x)

if "female" in student:
    print("female is pretty!")