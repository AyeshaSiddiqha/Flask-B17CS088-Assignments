import time
from functools import wraps
def my_timer(x):
    @wraps(x)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = x(*args, **kwargs)
        t2 = time.time() - t1
        print(' {} sec'.format( t2-t1))
        return result

    return wrapper

def my_logger(x):
    @wraps(x)
    def wrapper(*args, **kwargs):
       with open('log.txt','w') as y:
	        y.write(str(x(*args,**kwargs)))
       print("finished log")
    return wrapper


@my_timer
@my_logger
def add(x,y):
    time.sleep(1)
    return x+y
add(3,2)

