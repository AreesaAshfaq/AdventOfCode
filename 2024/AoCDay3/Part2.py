import re

# Open the file and read the input
d3 = open("2024_Day3_input.txt", "r")
p2 = 0
enabled = True  # Start with 'mul' instructions enabled

# Process each line from the input
for x in d3:
    # Regular expression patterns
    mul_pattern = r'mul\((\d+),(\d+)\)'  # To match mul(x, y)

    # Iterate through the string character by character
    index = 0
    while index < len(x):
        # Check for do() and don't() commands
        if x[index:index+4] == 'do()':
            enabled = True  # Enable 'mul' instructions
            index += 4  # Move index past do()
        elif x[index:index+7] == "don't()":
            enabled = False  # Disable 'mul' instructions
            index += 7  # Move index past don't()

        # Check for mul(x, y) instructions
        match = re.match(mul_pattern, x[index:])
        if match:
            x_val = int(match.group(1))
            y_val = int(match.group(2))
            if enabled:
                p2 += x_val * y_val  # Add result to p2 if enabled
            index += match.end()  # Move past the current match
        else:
            index += 1  # Move to next character

# Print the result after processing all lines
print(p2)
