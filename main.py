#list

food = ["pizza","burger","cake"]

food[0] = "sushi"

print(food[0])

food.append("ice cream")
food.remove("cake")
food.pop()
food.insert(0,"chicken")
food.sort()
food.clear()

for x in food:
    print(x)