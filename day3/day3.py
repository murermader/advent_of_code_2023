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


def part_two(lines: list[str]):
    def get_all_digits_coordinates_around(star_x, star_y):
        digit_coordinates = []

        coordinates_to_check = [
            # top left
            (star_x - 1, star_y - 1),
            # top
            (star_x, star_y - 1),
            # top right
            (star_x + 1, star_y - 1),

            # left
            (star_x - 1, star_y),
            # right
            (star_x + 1, star_y),

            # bottom left
            (star_x - 1, star_y + 1),
            # bottom
            (star_x, star_y + 1),
            # bottom right
            (star_x + 1, star_y + 1),
        ]

        # Debug
        # print(lines[coordinates_to_check[0][1]][coordinates_to_check[0][0]] +
        #       lines[coordinates_to_check[1][1]][coordinates_to_check[1][0]] +
        #       lines[coordinates_to_check[2][1]][coordinates_to_check[2][0]])
        # print(lines[coordinates_to_check[3][1]][coordinates_to_check[3][0]] +
        #       "*" +
        #       lines[coordinates_to_check[4][1]][coordinates_to_check[4][0]])
        # print(lines[coordinates_to_check[5][1]][coordinates_to_check[5][0]] +
        #       lines[coordinates_to_check[6][1]][coordinates_to_check[6][0]] +
        #       lines[coordinates_to_check[7][1]][coordinates_to_check[7][0]])

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

            if lines[y][x].isdigit():
                digit_coordinates.append((x, y))

        return digit_coordinates

    digits = []
    for y, line in enumerate(lines):
        for star_match in re.finditer(r"\*", line):
            digit_coordinates = get_all_digits_coordinates_around(star_match.start(), y)
            if len(digit_coordinates) < 2:
                # Need at least 2 numbers for it to be a gear
                continue

            gear_digits = set()
            for digit_x, digit_y in digit_coordinates:
                for digit_match in re.finditer(r"\d+", lines[digit_y]):
                    if digit_match.start() <= digit_x <= digit_match.end():
                        digit = int(digit_match.group(0))
                        gear_digits.add(digit)

            if len(gear_digits) == 2:
                gear_digits = list(gear_digits)
                digits.append(gear_digits[0] * gear_digits[1])

    print("Answer:", sum(digits))


if __name__ == '__main__':
    with open("input.txt", mode="r", encoding="utf-8-sig") as f:
        lines = [l.strip() for l in f.readlines()]

    part_one(lines)
    part_two(lines)
