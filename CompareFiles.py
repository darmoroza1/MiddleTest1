class CompareFiles:
    def __init__(self, file_name1: str, file_name2: str):
        with open(file_name1, 'r') as file_name1, open(file_name2, 'r') as file_name2:
            self.file1 = set(file_name1.readlines())
            self.file2 = set(file_name2.readlines())

    def compare_lines(self):
        """Compares the content of two files and returns the matching and differing lines."""
        same_lines = []
        diff_lines = []
        for line in self.file1:
            if line in self.file2 and line not in same_lines:
                same_lines.append(line)
            elif line not in diff_lines:
                diff_lines.append(line)
        for line in self.file2:
            if line not in same_lines and line not in diff_lines:
                diff_lines.append(line)
        return same_lines, diff_lines

    def write_results(self, same_lines: [str], diff_lines: [str]):
        """Writes the matching and differing lines to "same.txt" and "diff.txt" respectively."""
        with open("same.txt", "w") as same_file:
            same_file.writelines(same_lines)
        with open("diff.txt", "w") as diff_file:
            diff_file.writelines(diff_lines)
pass

