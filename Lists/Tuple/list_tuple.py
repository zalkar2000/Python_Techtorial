
t = (1,2,3,4,5,6)

# From this tuple remove each number if square of the number is smaller than 20

# Convert the tuple in to a list

t = list(t)

print(type(t))

# I have to remove each value 
l = t.copy()
for number in l:
    # 
    if number ** 2 < 20:
        t.remove(number)

t = tuple(t)
print(t)
print(type(t))