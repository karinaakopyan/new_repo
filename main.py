num1 = [*map(int, input("Enter number 1: "))]
num2 = [*map(int, input("Enter number 2: "))]

print(num1)
#num1 = num1[::-1]
print(num1)
#num2 = num2[::-1]


size = max(len(num1), len(num2))

num1 += [0] * (size - len(num1))
num2 += [0] * (size - len(num2))


overflow = 0
res = []
for obj in zip(num1, num2):
    value = obj[0] + obj[1] + overflow
    overflow = value // 2
    res.append(value % 2)

if overflow == 1:
    res.append(1)

res = res[::-1]

print(''.join(map(str, res)))


(1,1) (0,0) (1,1)
