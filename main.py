#if statement

age = int(input("What is your age?: "))

if age ==100:
    print("your are a century old!")
elif age >= 18:
    print("your are an adult!")
elif age <0:
    print("your haven't born yet!")
else:
    print("your are a child!")