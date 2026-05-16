from multiprocessing import Process


def compute(n):
    result = sum(i * i for i in range(n))
    print(f"Done computing {n}")


if __name__ == "__main__":
    numbers = [10 ** 6, 10 ** 7]
    processes = [Process(target=compute, args=(n,)) for n in numbers]
    for p in processes: p.start()
    for p in processes: p.join()
