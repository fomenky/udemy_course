def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

print methodception(add_two_numbers)
## OR
print methodception(lambda: 35 + 77)

my_list = [13, 56, 77, 484]
# Remove ONLY EVEN
print list(filter(lambda x: x != 13, my_list))


print (lambda x: x * 3)(5)

