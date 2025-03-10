import random
import time
import tracemalloc
import gc


def create_dna_string(length):
    return "".join(random.choice('AGCT') for index in range(length))


def read_dna_from_txt_file(file_path):
    with open(file_path, "r") as file:
        dna_string = "".join(line.strip() for line in file)
    return dna_string


def benchmark(func, dna, iterations=1):
    start = time.time()
    for iteration in range(iterations):
        func(dna)
    end = time.time()
    elapsed = (end - start) * 1000 / iterations
    return f"function {func.__name__}: time: {elapsed}, dna_length: {len(dna)}"


def benchmark_memory(func, dna):
    gc.disable()
    gc.collect()
    tracemalloc.start()
    func(dna)
    current, peak = tracemalloc.get_traced_memory()
    gc.enable()
    return f'Current Memory Usage: {current / 1024.0}KB', f'Peak Memory Usage: {peak / 1024.0}KB'
