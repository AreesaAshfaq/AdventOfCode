import re
d3 = open("2024_Day3_input.txt", "r")
p1 = 0
for x in d3:

  # Input string
  text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

  # Regular expression pattern to match mul(number, number) inside valid parentheses
  pattern = r'mul\((\d+),(\d+)\)'

  # Find all matches
  matches = [(int(match[0]), int(match[1])) for match in re.findall(pattern, x)]

  # Print the results
  for match in matches:
      mul = match[0] * match[1]
      p1 += mul
print(p1)
