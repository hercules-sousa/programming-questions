cards = int(input())
turns = int(input())
know_positions = list()
cards_dict = dict()

for i in range(turns):
    turn = input().split(" ")
    pos1 = turn[0]
    pos2 = turn[1]

    if pos1 not in know_positions:
        know_positions.append(pos1)
    if pos2 not in know_positions:
        know_positions.append(pos2)

    card1 = turn[2]
    card2 = turn[3]

    if card1 == card2:
        cards_dict[card1] = [pos1, pos2, True]
    else:
        if card1 not in cards_dict:
            cards_dict[card1] = [pos1]
        elif len(cards_dict[card1]) < 2 and pos1 not in cards_dict[card1]:
            cards_dict[card1].append(pos1)
        if card2 not in cards_dict:
            cards_dict[card2] = [pos2]
        elif len(cards_dict[card2]) < 2 and pos2 not in cards_dict[card2]:
            cards_dict[card2].append(pos2)


unknown_positions = cards - len(know_positions)
cards_without_pair = 0
may_be_matched = 0


for key in cards_dict:
    if len(cards_dict[key]) == 2:
        may_be_matched += 1
    elif len(cards_dict[key]) == 1:
        cards_without_pair += 1


if cards_without_pair == unknown_positions:
    may_be_matched += unknown_positions


if len(cards_dict.keys()) == cards / 2 - 1 and unknown_positions == 2:
    may_be_matched += 1

print(may_be_matched)
