import os
import argparse
import logging
from collections import namedtuple

logging.basicConfig(filename="log.txt", level=logging.INFO)

FileInfo = namedtuple(
    "FileInfo", ["name", "extension", "is_directory", "parent_directory"]
)


def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        parent_dir = os.path.basename(root)
        logging.info(f"Каталог обработки: {root}")

        for directory in dirs:
            file_info = FileInfo(directory, None, True, parent_dir)
            logging.info(f"Directory: {file_info}")

        for file in files:
            file_name, file_extension = os.path.splitext(file)
            file_info = FileInfo(file_name, file_extension, False, parent_dir)
            logging.info(f"File: {file_info}")


def main():
    parser = argparse.ArgumentParser(
        description="Обработка каталога и сбор информации о файлах."
    )
    parser.add_argument("каталог", help="Путь к директории")
    args = parser.parse_args()

    directory_path = args.directory
    process_directory(directory_path)


if __name__ == "__main__":
    main()
