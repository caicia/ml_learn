import time
from functools import wraps


def time_(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start_cpu = time.process_time()
        start_wall = time.perf_counter()
        out_ = func(*args, **kwargs)
        end_cpu = time.process_time()
        end_wall = time.perf_counter()

        print(f"CPU time: {end_cpu - start_cpu} s")
        print(f"Wall time: {end_wall - start_wall} s")

        return out_

    return wrap
