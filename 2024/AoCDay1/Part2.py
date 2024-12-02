d1 = open("/2024_Day1_input.txt", "r")
listL, listR, sum = [], [], 0
for x in d1:
  x1, x2 = x.split("  ")
  listL.append(int(x1))
  listR.append(int(x2))

for num in listL:
  countNum = listR.count(num)
  score = num * countNum
  sum += score
print(sum)
