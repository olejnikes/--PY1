list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


i = max(list_numbers)
last = list_numbers[-1]
list_numbers[-1] = i
list_numbers[9] = last

print(list_numbers)

