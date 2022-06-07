import random
from datetime import datetime
from time import sleep

def my_decorator(func):
    def execution_time():
        start_time = datetime.now()
        result = func()
        end_time = datetime.now()
        print(end_time - start_time)
        return result
    return execution_time

@my_decorator
def random_delay():
    sleep(random.randint(1, 5))

if __name__ == "__main__":
    random_delay()