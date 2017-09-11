# def timing(f):
#     def wrap(*args):
#         time1 = time.time()
#         ret = f(*args)
#         time2 = time.time()
#         print('%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0))
#         return ret
#     return wrap

#
#


import time

def my_decorator(some_function):
    def wrapper():
        start = time.time()
        some_function()
        end = time.time()
        print(end - start)
    return wrapper

@my_decorator
def just_some_function():
    print(1116636362931628918649182649184612911^33)

just_some_function()


#
# import time
#
# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)