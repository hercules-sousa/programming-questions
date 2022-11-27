entry = """
+---+---+---+---+---+---+---+---+
|.r.|:::|.b.|:q:|.k.|:::|.n.|:r:|
+---+---+---+---+---+---+---+---+
|:p:|.p.|:p:|.p.|:p:|.p.|:::|.p.|
+---+---+---+---+---+---+---+---+
|...|:::|.n.|:::|...|:::|...|:p:|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|.P.|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:P:|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|.P.|:::|.P.|:P:|...|:P:|.P.|:P:|
+---+---+---+---+---+---+---+---+
|:R:|.N.|:B:|.Q.|:K:|.B.|:::|.R.|
+---+---+---+---+---+---+---+---+
"""

positions = {
    "white": {},
    "black": {}
}

splitted_entry = entry.split("+---+---+---+---+---+---+---+---+")

for line_num in range(len(splitted_entry)):
    splitted_line = splitted_entry[line_num].split("|")
    if len(splitted_line) > 1:
        cleared_line = splitted_line[1: -1]
        for column_num in range(len(cleared_line)):
            pos = cleared_line[column_num]
            if pos[1] != ":" and pos[1] != ".":
                piece = pos[1]
                if piece.isupper():
                    print(piece, "White piece")
                else:
                    if piece not in positions["black"]:
                        positions["black"][piece] = []
                    positions["black"][piece].append("Teste")
                    print(piece, "Black piece")


print(positions)
