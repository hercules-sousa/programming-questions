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

print(ord("a"))
print(chr(97 + 1))

for line_num in range(len(splitted_entry)):
    splitted_line = splitted_entry[line_num].split("|")
    if len(splitted_line) > 1:
        cleared_line = splitted_line[1: -1]
        for column_num in range(len(cleared_line)):
            pos = cleared_line[column_num]
            if pos[1] != ":" and pos[1] != ".":
                piece = pos[1]
                if piece.isupper():
                    if piece not in positions["white"]:
                        positions["white"][piece] = []
                    positions["white"][piece].append(
                        f"{chr(97 + column_num)}{9 - line_num}")
                else:
                    if piece not in positions["black"]:
                        positions["black"][piece] = []
                    positions["black"][piece].append(
                        f"{chr(97 + column_num)}{line_num}")


print(positions["white"])
print(positions["black"])
