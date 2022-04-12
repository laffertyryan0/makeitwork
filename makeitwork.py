#this is kind of a joke, but I mean, go ahead and use it, I won't judge
def run_until_works(func):
    def wrapper(*args,**kwargs):
        return_val = None
        while(True):
            try:
                return_val = func(*args,**kwargs)
            except Exception as e:
                print("uh...")
            else:
                print("ok cool")
                break
        return return_val
    return wrapper

if __name__ == "__main__":
    import random

    #if you use this decorator @run_until_works when defining a function,
    #the code will keep trying to run until it stops erroring out
    @run_until_works
    def example():
        if random.random()>.1:
            assert 1 == 0
        else:
            return(5)

    print(example())
        
