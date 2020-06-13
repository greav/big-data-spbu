import argparse
import random
import sys

import tqdm

MAX_INT = 2 ** 32 - 1
FILE_SIZE = 2 * 1024 * 1024 * 1024  # in bytes
BYTES_PER_NUMBER = 4


def generate(file_name):
    with open(file_name, "wb") as f:
        for i in tqdm.tqdm(range(FILE_SIZE // BYTES_PER_NUMBER)):
            random_number = random.randint(0, MAX_INT)
            f.write(random_number.to_bytes(BYTES_PER_NUMBER, sys.byteorder))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out_file", type=str, default="numbers.bin",
    )
    namespace = parser.parse_args()
    generate(namespace.out_file)
