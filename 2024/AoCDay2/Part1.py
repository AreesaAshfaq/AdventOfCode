d2 = open("/2024_Day2_input.txt", "r")
totalSafeReports = 0

def isIncrease(level):
  for l in range(len(level)-1):
    diff = abs(level[l] - level[l+1])
    if level[l] < level[l+1] and diff >= 1 and diff <=3:
      continue
    else:
      return False
  return True
def isDecrease(level):
  for l in range(len(level)-1):
    diff = abs(level[l] - level[l+1])
    if level[l] > level[l+1] and diff >= 1 and diff <=3:
      continue
    else:
      return False 
  return True

for level in d2:
  curLevel = list(map(int, level.strip().split())) 
  if isIncrease(curLevel) or isDecrease(curLevel):
    totalSafeReports += 1
print(totalSafeReports)
