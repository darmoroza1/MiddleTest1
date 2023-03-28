def read_file(file_path):
    """Reads the contents of a file and returns them as a list of strings."""
    with open(file_path, "r") as file:
        contents = file.readlines()
    return contents

