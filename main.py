from CompareFiles import CompareFiles

check = CompareFiles("file1.txt", "file2.txt")


def compare_files():
    """Compares the content of two files and writes the matching
    and differing lines to "same.txt" and "diff.txt" respectively."""
    same_lines, diff_lines = check.compare_lines()
    check.write_results(same_lines, diff_lines)


compare_files()

