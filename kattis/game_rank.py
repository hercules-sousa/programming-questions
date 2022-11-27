games = list(input())

consecutive_wins = 0
current_rank = 25
stars = 0

for game in games:
    if game == "W":
        consecutive_wins += 1
        stars += 1
        if 6 <= current_rank <= 25 and consecutive_wins >= 3:
            stars += 1
        if 21 <= current_rank <= 25 and stars > 2:
            current_rank -= 1
            stars -= 2
        elif 16 <= current_rank <= 20 and stars > 3:
            current_rank -= 1
            stars -= 3
        elif 11 <= current_rank <= 15 and stars > 4:
            current_rank -= 1
            stars -= 4
        elif 1 <= current_rank <= 10 and stars > 5:
            current_rank -= 1
            stars -= 5
        if current_rank == 0:
            break
    else:
        consecutive_wins = 0

        if current_rank <= 20:
            stars -= 1
            if stars == -1:
                if current_rank == 20:
                    stars = 0
                else:
                    current_rank += 1
                    if current_rank >= 16:
                        stars = 2
                    elif current_rank <= 15 and current_rank >= 11:
                        stars = 3
                    elif current_rank <= 10 and current_rank >= 1:
                        stars = 4

    """ print("Game", game)
    print("Rank", current_rank)
    print("Estrelas", stars)
    print("Vitórias consecutivas", consecutive_wins)
    print() """


print("Legend" if current_rank == 0 else current_rank)
