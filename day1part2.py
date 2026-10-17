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

def partone(line):
    for line in content.strip.split("\n"):
        fw = None
        fd = ''
        ld = ''
        lw = None

        for word, num in replacements.items():
            pos = line.find(word)
            if pos != -1 and pos < first_pos:
                first_pos = pos
                first word = num

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


def replacement(line):
    for word, num in replacements.items():
        line = line.replace(num, word)
        print(line)


def main():
    with open("test.input.txt", "r") as inputval:
        content = replacement(inputval.read().strip())


if __name__ == "__main__":
    main()
