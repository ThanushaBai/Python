#exception handling


try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("u cant divide by zero")

except ValueError as e:
    print(e)
    print("enter only number plz")

except Exception as e:
    print(e)
    print("something went wrong:")
else:
    print(result)
finally:
    print("this is always execute")