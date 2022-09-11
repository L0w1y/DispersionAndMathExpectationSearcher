nums = []
cols = int(input("Введите колличество столбцов: "))
strings = int(cols/(cols/2))
firstString = []
secondString = []
mvl = []
mvi = []
print(strings)
for i in range(0, cols*2):
    nums.insert(i, float(input(f"Введите значение элемента {i+1}: ")))
for i in range(0, int(len(nums)-len(nums)/strings)):
    firstString.insert(i, float(nums[i]))
    # print(firstString)
for i in range(int(len(nums)/strings), int(len(nums))):
    secondString.insert(i, float(nums[i]))
    # print(secondString)
for i in range(len(firstString)):
    print(f"{firstString[i]} * {secondString[i]} = ",firstString[i]*secondString[i])
    mvl.append(firstString[i]*secondString[i])
for i in range(len(secondString)):
    print(f"{firstString[i]}^2 * {secondString[i]} = ",firstString[i]**2 * secondString[i])
    mvi.append(firstString[i]**2 * secondString[i])
print(f"Сумма первого столбца: {sum(mvl)}")
print(f"Сумма первого столбца в квадрате: {sum(mvl)**2}")
print(f"Сумма второго столбца: {sum(mvi)}")
print(f"Дисперсия или мат.ожидание: {sum(mvi)-sum(mvl)**2}")
# print(sum(mvi)-sum(mvl)**2)