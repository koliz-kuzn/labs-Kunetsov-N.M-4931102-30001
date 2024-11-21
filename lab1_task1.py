numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
i = 0
while numbers[i] is not None:
    i += 1
numbers[i] = sum(filter(None, numbers))/len(numbers)
print("Измененный список:", numbers)
