import re


def part_one(lines: list[str]):
    possible_game_ids = []

    for line in lines:
        m = re.match(r"Game (\d+): ", line)
        game_id = int(m.group(1))

        # Remove part with game information
        line = line[m.end():]
        game_is_possible = []

        # Count number of cubes in each part of the game
        for i, game_part in enumerate(line.split(";")):
            blue = 0
            green = 0
            red = 0

            if m := re.search(r"(\d+) blue", game_part):
                blue = int(m.group(1))
            if m := re.search(r"(\d+) green", game_part):
                green = int(m.group(1))
            if m := re.search(r"(\d+) red", game_part):
                red = int(m.group(1))

            game_is_possible.append(red <= 12 and green <= 13 and blue <= 14)

        if all(game_is_possible):
            possible_game_ids.append(game_id)

    print("Answer:", sum(possible_game_ids))


def part_two(lines: list[str]):
    cube_sets = []

    for line in lines:
        m = re.match(r"Game (\d+): ", line)

        # Remove part with game information
        line = line[m.end():]

        min_blue = 0
        min_green = 0
        min_red = 0

        # Count number of cubes in each part of the game
        for i, game_part in enumerate(line.split(";")):
            if m := re.search(r"(\d+) blue", game_part):
                blue = int(m.group(1))
                if blue > min_blue:
                    min_blue = blue
            if m := re.search(r"(\d+) green", game_part):
                green = int(m.group(1))
                if green > min_green:
                    min_green = green
            if m := re.search(r"(\d+) red", game_part):
                red = int(m.group(1))
                if red > min_red:
                    min_red = red

        cube_sets.append((min_blue, min_green, min_red))

    answer = 0
    for b, g, r in cube_sets:
        answer += b * g * r

    print(f"Answer: {answer}")


if __name__ == '__main__':
    with open("input.txt", mode="r", encoding="utf-8-sig") as f:
        lines = [l.strip() for l in f.readlines()]

    part_one(lines)
    part_two(lines)
