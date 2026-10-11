replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
 }
with open("input.txt", "r") as inputval:
    content = inputval.read()

def parttwo(line):
    total = 0
    result=[]
    for i in range(len(line)):
        if line[i].isdigit():
            result.append(line[i])
        for word, value in replacements.items():
            if line[i:].startswith(word):
                result.append(int(value))
    if not result:
        return 0
    first_digit_int = result[0]
    last_digit_int = result[-1]
    return (int(first_digit_int) * 10) + int(last_digit_int)

def main():
    with open("test.input.txt", "r") as inputval:
        content = inputval.read()

part2_answer = 0

for line in content.splitlines():
    val = parttwo(line)
    print(f"Line: {line!r} -> {val}")
    part2_answer += val

print(part2_answer)


if __name__ == "__main__":
    main()
