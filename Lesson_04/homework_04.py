import os
from pathlib import Path
from typing import Generator

from pympler import asizeof

LESSON_4_DIR = Path(__file__).parent
ROCKYOU_FILENAME = LESSON_4_DIR / "rockyou.txt"
RESULT_FILENAME = LESSON_4_DIR / "result.txt"
USER_PATTERN = input("Please, enter the keyword to search in file: ")


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline().replace("\n", "")

            if not line:
                break

            if pattern in line.lower():
                yield line


def lines_writer_to_file(path_to_file, filtered_items) -> None:
    if asizeof.basicsize(path_to_file) > 0:
        os.remove(path_to_file)
    with open(path_to_file, "a", encoding="utf-8") as result_file:
        for item in filtered_items:
            result_file.write(item + "\n")


def lines_counter(input_file) -> int:
    with open(input_file) as file:
        return sum(1 for _ in file)


def size_counter(input_file) -> int:
    return asizeof.basicsize(input_file)


def main():
    filtered_items = list(filter_lines(ROCKYOU_FILENAME, USER_PATTERN))
    lines_writer_to_file(RESULT_FILENAME, filtered_items)
    total_lines = lines_counter(RESULT_FILENAME)
    file_size = size_counter(RESULT_FILENAME)
    if total_lines == 0:
        print(
            f"Seems, like we found nothing in {ROCKYOU_FILENAME}. "
            f"Please, try again with another request"
        )
    elif total_lines > 0:
        print(
            f"There are {total_lines} lines in {RESULT_FILENAME},"
            f" \nFile size is: {file_size} kb"
        )


if __name__ == "__main__":
    main()
