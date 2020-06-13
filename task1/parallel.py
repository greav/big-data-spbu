import argparse
import mmap
import multiprocessing
import os
import sys
import time

N_PROCESSES = multiprocessing.cpu_count()
BYTES_PER_NUMBER = 4


def process_chunk(chunk):
    min_number, max_number, sum_ = float("inf"), float("-inf"), 0

    for idx in range(0, len(chunk), BYTES_PER_NUMBER):
        number = int.from_bytes(
            chunk[idx : idx + BYTES_PER_NUMBER], byteorder=sys.byteorder
        )
        min_number = min(number, min_number)
        max_number = max(number, max_number)
        sum_ += number
    return min_number, max_number, sum_


def chunks(data, n_chunks):
    chunksize = len(data) // n_chunks
    for i in range(0, len(data), chunksize):
        yield data[i : i + chunksize]


def parallel_aggregation(bin_file, n_chunks):
    with open(bin_file, "rb") as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.MAP_SHARED) as mm:
            pool = multiprocessing.Pool(processes=None)
            results = pool.imap(process_chunk, chunks(mm, n_chunks=n_chunks))
            mins, maxs, sums = zip(*results)
            min_number, max_number, sum_ = min(mins), max(maxs), sum(sums)

    return min_number, max_number, sum_


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bin_file", type=str, default="numbers.bin",
    )
    parser.add_argument(
        "--profiling_file", type=str, default="profiling.txt",
    )
    parser.add_argument(
        "--n_chunks", type=int, default=N_PROCESSES,
    )
    namespace = parser.parse_args()

    if not os.path.exists(namespace.bin_file):
        raise FileNotFoundError(f"{namespace.bin_file} not found")

    start_time = time.perf_counter()
    min_number, max_number, sum_ = parallel_aggregation(
        namespace.bin_file, namespace.n_chunks
    )
    total_time = time.perf_counter() - start_time

    with open(namespace.profiling_file, "a") as f:
        msg = (
            f"parallel >>> total time: {total_time} seconds, "
            f"min_number: {min_number}, max_number: {max_number}, "
            f"sum: {sum_}, n_processes: {N_PROCESSES}"
        )
        f.write(f"{msg}\n")


if __name__ == "__main__":
    main()
