f = open("contact_db.txt", "rt")
print(f.readlines())

lines = f.readlines()

# print(lines)


print(len(f.readlines()))


num = len(lines)/4

num = int(num)

# print(len(lines))