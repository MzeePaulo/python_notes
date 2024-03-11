#For Loop
friends = ["Sos", "Chris", "Charles"]
for friend in friends:
    print(friend)

#Example 2
for index in range(10):
    print(index)

#Example 3
for index in range(100):
    print(index/2)

#Example 4
for index in range(2,12):
    print(index)

#Example 5
friends = ["Sos", "Chris", "Charles"]
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")

#Exponent function

print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3,3))
