import time
from functools import wraps

def rate_limiter(interval):
 
    def decorator(func):
        last_called = [0] 
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            elapsed_time = current_time - last_called[0]
            
            if elapsed_time >= interval:
                last_called[0] = current_time
                return func(*args, **kwargs)
            else:
                print(f"Функция вызвана слишком рано. Подождите {interval - elapsed_time:.2f} секунд.")
        
        return wrapper
    return decorator

@rate_limiter(2) 
def my_function():
    print("Функция выполнена!")


my_function()  
time.sleep(1)
my_function() 
time.sleep(2)
my_function()  