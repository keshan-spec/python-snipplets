# Append vs. Extends

# Append : adds one new element
a = [1, 2, 3, 4]
a1 = [7, 8]
a.append(a1)
print(a)  # [1, 2, 3, 4 , [7, 8]]

# Extend : adds one new element
b = [1, 2, 3, 4]
b1 = [7, 8]
b.extend(b1)
print(b)  # [1, 2, 3, 4 , 7, 8]
