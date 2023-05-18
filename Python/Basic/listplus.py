lucky_numbers=[4,5,8,5,3]
friends=["Wako","Tako","Yago","Backham"]
friends.extend(lucky_numbers)
print(friends)

friends.append("Roger")
print(friends)


friends.insert(1,"Harden")
print(friends)


friends.remove("Tako")
print(friends)


friends.pop()
print(friends)

print(friends.index("Ya"))
print(friends)

friends.clear()
print(friends)

