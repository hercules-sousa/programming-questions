cards = input()

cards_dict = {
    "P": {
        "n": 13,
        "cards": []
    },
    "K": {
        "n": 13,
        "cards": []
    },
    "H": {
        "n": 13,
        "cards": []
    },
    "T": {
        "n": 13,
        "cards": []
    }
}

for i in range(0, len(cards), 3):
    card = cards[i + 1: i + 3]
    if card not in cards_dict[cards[i]]["cards"]:
        cards_dict[cards[i]]["cards"].append(card)
        cards_dict[cards[i]]["n"] -= 1
    else:
        print("GRESKA")

print(cards_dict)
