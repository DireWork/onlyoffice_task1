import main
import os
import random

def test_tree():

    file_path = "tree.txt"
    levels = random.randint(1,10)

    main.create_tree(levels, file_path)

    assert os.path.exists(file_path)

    with open(file_path, 'r') as f:
        lines = f.readlines()

    expected_lines = 4 + levels
    assert len(lines) == expected_lines

test_tree()