
# 第一級関数
import inspect


def first_class_functions():
    print(inspect.currentframe().f_code.co_name)
    
    # 関数を変数に代入
    def greet(name):
        return f"Hello, {name}"
    
    say_hello = greet
    print(say_hello("Alice"))  # Hello, Alice

    # 関数を引数に渡す
    def call_with_name(func, name):
        return func(name)
    
    print(call_with_name(greet, "Bob"))  # Hello, Bob

    # 関数を返す
    def make_greeting(greeting):
        def greet(name):
            return f"{greeting}, {name}"
        return greet
    
    say_hi = make_greeting("Hi")
    print(say_hi("Carol"))  # Hi, Carol
    
def first_class_functions2():
    print(inspect.currentframe().f_code.co_name)

    def apply(func, value):
        return func(value)
    
    def double(x):
        return x * 2
    
    def square(x):
        return x * x
    
    print(apply(double, 5))   # 10
    print(apply(square, 5))   # 25

def first_class_functions3():
    print(inspect.currentframe().f_code.co_name)

    def multiplier(n):
        def inner(x):
            return x * n
        
        return inner
    
    double = multiplier(2)
    triple = multiplier(3)
    
    print(double(5))  # 10
    print(triple(5))  # 15
    

def closure():
    print(inspect.currentframe().f_code.co_name)
    
    def multiplier(n):
        def inner(x):
            return x * n   # ← nはinnerのスコープにないのに使える！
        return inner

    double = multiplier(2)
    # multiplier の実行は終わったのに、n=2 が記憶されている
    print(double(4))   # 8
    
    print(double.__closure__)  # (cell at 0x7f8c9c0b1e50: int)  ← n=2 がクロージャで保持されている
    print(double.__closure__[0].cell_contents)  # 2
    
    def make_tax_calculator(rate):
        def calc(price):
            return price * (1 + rate)
        
        return calc
        
    calc_normal = make_tax_calculator(0.1)
    calc_reduced = make_tax_calculator(0.08)
        
    print(calc_normal(1000))
    print(calc_reduced(1000))

def closure2():
    print(inspect.currentframe().f_code.co_name)
    
    def make_counter():
        count = 0
        
        def counter():
            nonlocal count
            count += 1
            return count
        
        return counter
    
    c1 = make_counter()
    c2 = make_counter()
    
    print(c1())  # 1
    print(c1())  # 2
    print(c2())  # 1 (c2は別のクロージャなので独立している)
    
    
def decorator():
    print(inspect.currentframe().f_code.co_name)
    
    def log_calls(func):
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} with args={args} kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        
        return wrapper
    
    @log_calls
    def add(x, y):
        return x + y
    
    print(add(3, 4))  # ログが出力されてから7が出力される 

def decorator2():
    print(inspect.currentframe().f_code.co_name)
    
    import time

    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__}: {end - start:.3f}秒")
            return result
        
        return wrapper

    @timer
    def heavy_process():
        time.sleep(1)

    heavy_process()  # heavy_process: 1.001秒
    
def decorator3():
    print(inspect.currentframe().f_code.co_name)
    
    def cache(func):
        stored ={}
        def wrapper(*args, **kwargs):
            if args in stored:
                print(f"args={args}, result={stored[args]}")
                return stored[args]
            
            result = func(*args)
            stored[args] = result
            return result
        
        return wrapper
            
    @cache
    def heavy_calc(n):
        import time
        time.sleep(1)
        return n * 2
    
    heavy_calc(2)
    heavy_calc(3)
    heavy_calc(2)
    heavy_calc(3)
    heavy_calc(3)
    heavy_calc(2)
    heavy_calc(2)
    
def decorator4():
    from functools import lru_cache
    @lru_cache(maxsize=128)
    def fibonacci(n):
        if n<2:
            return n
        
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(fibonacci(10))
    
if __name__ == "__main__":
    #first_class_functions()
    #first_class_functions2()
    #first_class_functions3()
    #closure()
    #closure2()
    #decorator()
    #decorator2()
    #decorator3()
    decorator4()
