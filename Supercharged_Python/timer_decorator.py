# Supercharged Python, page 130

import time

def make_timer(func):
    def wrapper(*args, **kwargs):        # wrapped function replaces orginal function
        t1 = time.time()
        ret_val = func(*args, **kwargs)  # Run orginal function with any arguments it was given
        t2 = time.time()
        print('Time elapsed:', t2 - t1) 
        return ret_val                   # Return response from original function
    return wrapper


@make_timer         # Wrap count_nums function with make_timer decorator / Can comment out without affecting script
def count_nums(n):  # Count lots of numbers without generating any output
    for i in range(n):
        for j in range(1000):
            pass 
# '@make_timer' before count_nums function is equivalent to 'count_nums = make_timer(count_nums)' after the count_nums function

count_nums(33000)

