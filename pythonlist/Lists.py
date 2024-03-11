
lucky_numbers = [2, 8, 6, 7, 23, 57]
friends = ["Ian", "Rose", "Shaline", "Charles", "Chris", "Sos", "Charles"]

print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
friends[1] = "Grace"
print(friends[1])
print(friends[1:3])
friends.sort()
print(friends)

#Lists Functions
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)
friends.extend(lucky_numbers)
print(friends)
friends.append("Zoo")
friends.insert(1, "Ruth")
print(friends)
friends.remove("Ruth")
friends.pop()
print(friends.index("Sos"))
print(friends.count("Charles"))
friends2 = friends.copy()
print(friends2)
friends.clear()
print(friends)
