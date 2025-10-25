#set

utensils = {"spoon","fork","knife"}
dishes ={"bowl","plate","cup"}

utensils.remove("spoon")
utensils.add("spoon")
utensils.clear()
utensils.update(dishes)
dishes.update(utensils)
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)