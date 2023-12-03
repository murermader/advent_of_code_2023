import re


def part_one(lines: list[str]):
    def check_for_symbol(x, y):
        # y - 1
        # y
        # y + 1
        coordinates_to_check = [
            # top
            (x, y - 1),
            # left
            (x - 1, y),
            # right
            (x + 1, y),
            # bottom
            (x, y + 1),

            # top left
            (x - 1, y - 1),
            # top right
            (x + 1, y - 1),
            # bottom right
            (x + 1, y + 1),
            # bottom left
            (x - 1, y + 1),
        ]

        for x, y in coordinates_to_check:
            if y >= len(lines):
                # Out of bounds: top
                continue

            if y < 0:
                # Out of bounds: bottom
                continue

            if x < 0:
                # Out of bounds: left
                continue

            if x >= len(lines[y]):
                # Out of bounds: right
                continue

            char = lines[y][x]

            if re.match(r"[^.\d]", char):
                return True

        return False

    def check_around_digit(m: re.Match):
        for x in range(m.start(), m.end()):
            if check_for_symbol(x, y):
                return int(digit_match.group(0))
        return None

    digits = []
    for y, line in enumerate(lines):
        for digit_match in re.finditer(r"\d+", line):
            if digit := check_around_digit(digit_match):
                digits.append(digit)

    print("Answer:", sum(digits))


if __name__ == '__main__':
    with open("input.txt", mode="r", encoding="utf-8-sig") as f:
        lines = [l.strip() for l in f.readlines()]

    part_one(lines)
