import argparse
import os
import sys
import time

BYTES_PER_NUMBER = 4


def sequential_aggregation(bin_file):
    min_number, max_number, sum_ = float("inf"), float("-inf"), 0
    with open(bin_file, "rb") as f:
        bytes_ = f.read(BYTES_PER_NUMBER)
        while bytes_:
            number = int.from_bytes(bytes_, byteorder=sys.byteorder)
            min_number = min(number, min_number)
            max_number = max(number, max_number)
            sum_ += number
            bytes_ = f.read(BYTES_PER_NUMBER)
    return min_number, max_number, sum_


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bin_file", type=str, default="numbers.bin",
    )
    parser.add_argument(
        "--profiling_file", type=str, default="profiling.txt",
    )
    namespace = parser.parse_args()

    if not os.path.exists(namespace.bin_file):
        raise FileNotFoundError(f"{namespace.bin_file} not found")

    start_time = time.perf_counter()
    min_number, max_number, sum_ = sequential_aggregation(namespace.bin_file)
    total_time = time.perf_counter() - start_time

    with open(namespace.profiling_file, "a") as f:
        msg = (
            f"sequential >>> total time: {total_time} seconds, "
            f"min_number: {min_number}, max_number: {max_number}, sum: {sum_}"
        )
        f.write(f"{msg}\n")


if __name__ == "__main__":
    main()
