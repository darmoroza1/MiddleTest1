import pytest
import tempfile
import os

from CompareFiles import CompareFiles


@pytest.fixture
def file_paths():
    # Створення тимчасових файлів
    file1_handle, file1_path = tempfile.mkstemp()
    file2_handle, file2_path = tempfile.mkstemp()
    os.close(file1_handle)
    os.close(file2_handle)

    # Запис вмісту у файли
    file1_contents = ["line 1\n", "line 2\n", "line 3\n"]
    file2_contents = ["line 1\n", "line 3\n", "line 4\n"]
    with open(file1_path, "w") as file1, open(file2_path, "w") as file2:
        file1.writelines(file1_contents)
        file2.writelines(file2_contents)

    yield file1_path, file2_path

    # Видалення тимчасових файлів
    os.remove(file1_path)
    os.remove(file2_path)


@pytest.fixture
def file_comparator(file_paths):
    # Створення екземпляру класу FileComparator
    file1_path, file2_path = file_paths
    comparator = CompareFiles(file1_path, file2_path)
    return comparator
