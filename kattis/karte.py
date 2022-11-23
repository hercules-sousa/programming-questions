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

error = False
for i in range(0, len(cards), 3):
    card = cards[i + 1: i + 3]
    if card not in cards_dict[cards[i]]["cards"]:
        cards_dict[cards[i]]["cards"].append(card)
        cards_dict[cards[i]]["n"] -= 1
    else:
        error = True
        break

if not error:
    result = str()
    counter = 0
    for key in cards_dict:
        if counter < 3:
            result += str(cards_dict[key]["n"]) + ' '
        else:
            result += str(cards_dict[key]["n"])
        counter += 1
    print(result)
else:
    print("GRESKA")
