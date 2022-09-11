
numsstorage = [float]
colls = int

colls = int(input("Enter colls count here: "))

def Calculate(nums:[float], cls:int):
    col1 = [float]
    for i in range(0, cls):
        col1.insert(i, nums[i])

for i in range(0, colls*2):
    num = float(input("Enter a num for first string"))
    numsstorage.insert(i, num)

bool = bool(input("Do you want continue?(True/False): "))
if bool:
    Calculate()