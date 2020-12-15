import time
import functools

def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    return wrapper

@cache
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)

def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print('Without Decorator')
start = time.perf_counter();
fibonacci(20);
print('Fib 20 Time run: ', time.perf_counter() - start)

start = time.perf_counter(); 
fibonacci(30); 
print('Fib 30 Time run:', time.perf_counter() - start,'\n')

print('With Decorator')
start = time.perf_counter();
fib(20);
print('Fib 20 Time run: ', time.perf_counter() - start)

start = time.perf_counter(); 
fib(30); 
print('Fib 30 Time run:', time.perf_counter() - start)
