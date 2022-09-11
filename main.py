colls = int(input("Введите колличество столбцов: "))
print(f"Колличество элементов == {colls*2}")
firtststring = []   # −1   2   5  10   20
secondstring = []   # 0.1 0.2 0.3 0.3 0.1
MathematicalExpectation = []
SquaredFirstString = []
DispercyMultiplier = []
def Frac(i):
    try:
        return float(i)
    except ValueError:
        n, d = i.split('/')
        return float(n)/float(d)
for i in range(0, colls):
    firtststring.insert(i, Frac(input("1 : ")))
for i in range(0, colls):
    secondstring.insert(i, Frac(input("2 : ")))
print()
print("="*30)
print()
for i in range(0, len(firtststring)):
    print(f" : {firtststring[i]} * {secondstring[i]} = {firtststring[i]*secondstring[i]}")
    MathematicalExpectation.insert(i, float(firtststring[i]*secondstring[i]))
MathematicalExpectation = sum(MathematicalExpectation)
print()
print(f"Мат.Ожидание == {MathematicalExpectation}")
print()
for i in range(0, colls):
    print(f" : {firtststring[i]}^2 * {secondstring[i]} = {firtststring[i]**2 * secondstring[i]}")
    SquaredFirstString.insert(i, firtststring[i]**2 * secondstring[i])
SquaredFirstString = sum(SquaredFirstString)
print()
print(f" : {SquaredFirstString} - {MathematicalExpectation}^2 == {SquaredFirstString - MathematicalExpectation**2}")
print()
print(f"Квадратичное Мат.Ожидание == {SquaredFirstString}")
print(f"Дисперсия == {SquaredFirstString - MathematicalExpectation**2}")