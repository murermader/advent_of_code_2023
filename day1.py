import re


def part_one():
    with open("day1_input.txt", mode="r", encoding="utf-8-sig") as f:
        lines = f.readlines()

    numbers = []

    for line in lines:

        left_number = None
        right_number = None
        for c in line:
            if m := re.match(r"\d", c):
                left_number = m.group(0)
                break

        for c in line[::-1]:
            if m := re.match(r"\d", c):
                right_number = m.group(0)
                break

        number = int(left_number + right_number)
        numbers.append(number)

    answer = sum(numbers)
    print("Answer:", answer)


def part_two():
    with open("day1_input.txt", mode="r", encoding="utf-8-sig") as f:
        lines = [l.strip() for l in f.readlines()]

    numbers = []

    def get_number(line: str, reverse: bool):
        numbers_as_text = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }

        if reverse:
            pattern = rf"({'|'.join([n[::-1] for n in numbers_as_text.keys()])})"
        else:
            pattern = rf"({'|'.join(numbers_as_text.keys())})"

        if reverse:
            line = line[::-1]

        for i in range(len(line)):
            # Try number
            if m := re.match(r"\d", line[i]):
                return m.group(0)

            # Try word
            if m := re.match(pattern, line[i:]):
                if reverse:
                    return str(numbers_as_text[m.group(0)[::-1]])
                else:
                    return str(numbers_as_text[m.group(0)])

    for line in lines:
        left_number = get_number(line, False)
        right_number = get_number(line, True)
        number = int(left_number + right_number)
        numbers.append(number)

    answer = sum(numbers)
    # for number in numbers:
    #     print(number)
    print("Answer:", answer)


if __name__ == '__main__':
    part_one()
    part_two()
