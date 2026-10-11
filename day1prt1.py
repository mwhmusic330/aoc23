def main():
    with open("input.txt", "r") as inputval:
        content = inputval.read()
    result = 0

    for line in content.strip().split("\n"):
        print(line)
        fd = ''
        ld = ''

        for char in line:
            if char.isdigit():
                fd=char
                break
        for char in line[::-1]:
            if char.isdigit():
                ld=char
                break
        result = result + int(fd + ld)
        print(result)


if __name__ == "__main__":
    main()
