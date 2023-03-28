import os
from CompareFiles import CompareFiles

def test_compare_lines():
    # Set up
    file1_contents = ["line 1\n", "line 2\n", "line 3\n"]
    file2_contents = ["line 1\n", "line 3\n", "line 4\n"]
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    with open(file1_path, "w") as file1, open(file2_path, "w") as file2:
        file1.writelines(file1_contents)
        file2.writelines(file2_contents)
    comparator = CompareFiles(file1_path, file2_path)

    same_lines, diff_lines = comparator.compare_lines()

    assert same_lines == ["line 1\n", "line 3\n"]
    assert diff_lines == ["line 2\n", "line 4\n"]

    os.remove(file1_path)
    os.remove(file2_path)
