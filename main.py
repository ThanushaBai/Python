#logical operators (and ,or, not)

temp = int(input("what is the temperature outside?:"))

if not(temp >= 0 and temp <= 30):
    print("the temperature is bad today!")
    print("go outside!")

elif not(temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("stay inside!")

