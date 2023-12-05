import re
from collections import Counter
from dataclasses import dataclass
from queue import Queue, PriorityQueue


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


# @dataclass(order=True)
# class Card:
#     def __init__(self, id, other_card_ids: list[int]):
#         self.id = id
#         self.other_card_ids = other_card_ids
        # self.winning_numbers = winning_numbers
        # self.our_numbers = our_numbers

    # def __repr__(self):
    #     return f"ID={self.id} Number of Matches={len(self.get_matching_numbers())}"

    # def get_matching_numbers(self):
    #     numbers = []
    #     for number in self.our_numbers:
    #         if number in self.winning_numbers:
    #             numbers.append(number)
    #     return numbers


def part_two(lines: list[str]):
    cards: dict[int, list[int]] = {}
    cards_queue = PriorityQueue()
    cards_counter = Counter()

    print("Setup:")
    for line in lines:
        line = line.replace("Card ", "")
        card_id, numbers_str = line.split(":", 2)
        card_id = int(card_id)

        winning_numbers_str, our_numbers_str = line.split("|", 2)
        winning_numbers = []
        our_numbers = []
        for number in re.findall(r"(\d+)", winning_numbers_str):
            winning_numbers.append(number)
        for number in re.findall(r"(\d+)", our_numbers_str):
            our_numbers.append(number)

        numbers = []
        for number in our_numbers:
            if number in winning_numbers:
                numbers.append(number)

        other_card_ids = []
        for i, _ in enumerate(numbers):
            other_card_id = card_id + i + 1
            # copied_card = cards[copy_card_with_id]
            # print(f"Add card {copied_card.id} to queue")
            # cards_queue.put(copy_card_with_id)
            other_card_ids.append(other_card_id)

        print(f"Card ID={card_id} Other Card IDs={', '.join([str(id) for id in other_card_ids])}")
        # card = Card(card_id, other_card_ids)
        cards[card_id] = other_card_ids
        cards_queue.put(card_id)

    counter = {card_id: 0 for card_id in cards.keys()}

    current_card = None

    print("Loop:")
    while not cards_queue.empty():
        card_id = cards_queue.get()

        if current_card != card_id:
            current_card = card_id
            print(f"Current Card: {card_id}")

        other_cards = cards[card_id]
        # Count how many times we have seen this card
        # cards_counter.update(str(card_id))
        counter[card_id] = counter[card_id] + 1

        # print(f"[{card_id}] Add {len(other_cards)}")
        for other_card_id in other_cards:
            # copy_card_with_id = other_cards.id + i + 1
            # copied_card = cards[copy_card_with_id]
            # print(f"Add card {copied_card.id} to queue")
            cards_queue.put(other_card_id)
        # print(f"Card: {card.id}: {len(card.get_matching_numbers())}")

    # print(cards_counter)
    print(f"Answer: {sum(counter.values())}")


if __name__ == '__main__':
    with open("input.txt", mode="r", encoding="utf-8-sig") as f:
        lines = [l.strip() for l in f.readlines()]

    # part_one(lines)
    part_two(lines)
