def create_tree(levels, file_path):
    with open(file_path, 'w') as f:
        # Верхушка
        f.write(" " * (levels * 2-1) + "W\n")
        f.write(" " * (levels * 2-1) + "*\n")

        # Основная часть ёлки
        for i in range(0, levels):
            count_start = 5
            line = ''

            stars = "*" * (count_start + i * 4)

            if i % 2 == 0:
                line = stars + '@' + "\n"
            else:
                line = '@' + stars + "\n"

            # Отступы для каждого уровня
            padding = " " * ((levels-i-1)*2-1)
            f.write(padding + line)

        # Ствол ёлки
        trunk = " " * (levels * 2-round(levels/2)) + "T"*levels+"\n"
        f.write(trunk)
        f.write(trunk)

# create_tree(7, 'tree.txt')