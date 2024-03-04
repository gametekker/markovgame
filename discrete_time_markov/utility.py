import time
import functools


def print_time_in_color(should_print=True, color="green"):
    color_codes = {
        "green": "\033[92m",  # Green
        "red": "\033[91m",  # Red
        "bold": "\033[1m",  # Bold
        "end": "\033[0m",  # Reset
    }

    def decorator(func):
        # Use a dictionary to keep track of recursive calls
        in_call = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if in_call.get(func, False):
                # This is a recursive call, simply proceed with the function
                return func(*args, **kwargs)

            in_call[func] = True  # Mark as in a call

            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            in_call[func] = False  # Reset the flag after function execution

            if should_print:
                elapsed_time = end_time - start_time
                print(
                    f"{color_codes['bold']}{color_codes[color]}Execution time of {func.__name__}: {elapsed_time:.4f} seconds{color_codes['end']}")

            return result

        return wrapper

    return decorator