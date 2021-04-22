lst = [1, 2, 3, 4]
new_dict = current_dict = {}
for num in lst:
    current_dict[num] = {}
    current_dict = current_dict[num]
print(new_dict)