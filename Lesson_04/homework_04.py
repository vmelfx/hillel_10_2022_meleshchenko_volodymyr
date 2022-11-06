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


def lines_writer_to_file() -> None:
    for item in filtered_items:
        with open(RESULT_FILENAME, "a", encoding="utf-8") as result_file:
            result_file.write(item + "\n")


def lines_counter(input_file) -> int:
    with open(input_file) as file:
        return sum(1 for _ in file)


def size_counter(input_file):
    return asizeof.basicsize(input_file)


filtered_items = list(filter_lines(ROCKYOU_FILENAME, USER_PATTERN))

print(lines_counter(RESULT_FILENAME))
print(size_counter(RESULT_FILENAME))
print(len(filtered_items))
