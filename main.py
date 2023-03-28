def read_file(file_path):
    """Reads the contents of a file and returns them as a list of strings."""
    with open(file_path, "r") as file:
        contents = file.readlines()
    return contents


def compare_lines(lines1, lines2):
    """Compares the content of two files and returns the matching and differing lines."""
    same_lines = []
    diff_lines = []
    for line in lines1:
        if line in lines2 and line not in same_lines:
            same_lines.append(line)
        elif line not in diff_lines:
            diff_lines.append(line)
    for line in lines2:
        if line not in same_lines and line not in diff_lines:
            diff_lines.append(line)
    return same_lines, diff_lines



