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
        fw = None
        fd = len(line)
        ld = -1
        lw = None

        for word, num in replacements.items():
            pos = line.find(word)
            if pos != -1 and pos < fd:
                fd = pos
                fw = num
            pos = line.rfind(word)
            if pos != -1 and pos > ld:
                ld = pos
                lw = num
        if fw is None:
            return 0
        return int(fw) * 10 + int(lw)
                

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
        return line

def main():
    with open("input.txt", "r") as inputval:
        content = replacement(inputval.read().strip())
    converted = replacement(content)
    total = 0
    for line in converted.split("\n"):
        total += partone(line)
    print(total)


if __name__ == "__main__":
    main()
