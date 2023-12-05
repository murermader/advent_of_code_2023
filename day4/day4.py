import re


def part_one(lines: list[str]):

    total_points = 0
    for line in lines:
        # Remove Card info
        line = line.split(":")[1]

        winning_numbers_str, our_numbers_str = line.split("|", 2)

        winning_numbers = []
        our_numbers = []

        for number in re.findall(r"(\d+)", winning_numbers_str):
            winning_numbers.append(number)

        for number in re.findall(r"(\d+)", our_numbers_str):
            our_numbers.append(number)

        points = 0

        for number in our_numbers:
            if number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points = points * 2

        total_points += points

    print(f"Answer: {total_points}")


def part_two(lines: list[str]):
    ...


if __name__ == '__main__':
    with open("input.txt", mode="r", encoding="utf-8-sig") as f:
        lines = [l.strip() for l in f.readlines()]

    part_one(lines)
    part_two(lines)
