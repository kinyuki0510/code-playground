import inspect
import time

def context_manager():
    print(inspect.currentframe().f_code.co_name)
    
    class Timer:
        def __enter__(self):
            self.start = time.time()
            return self             # as で受け取る値

        def __exit__(self, exc_type, exc_val, exc_tb):
            elapsed = time.time() - self.start
            print(f"経過時間: {elapsed:.3f}秒")
            return False            # 例外を握りつぶさない

    with Timer() as t:
        time.sleep(1)
        
def context_manager2():
    print(inspect.currentframe().f_code.co_name)
    
    from contextlib import contextmanager

    @contextmanager
    def timer():
        try:
            start = time.time()
            yield
        finally:
            elapsed = time.time() - start
            print(f"経過時間: {elapsed:.3f}秒")

    with timer():
        time.sleep(1)
        raise ValueError("例外発生！")

def class_and_oop():
    print(inspect.currentframe().f_code.co_name)
    
    class User:
        def __init__(self, name, age):
            self.name = name
            self._age = age
            self.__id = id(self)  # プライベート属性（名前修飾される）

        def greet(self):
            print(f"Hello, I'm {self.name} and I'm {self._age} years old.")
            
        @property
        def age(self):
            return self._age
        
        @age.setter
        def age(self, value):
            if value < 0:
                raise ValueError("年齢は0以上でなければなりません")
            
            self._age = value

    alice = User("Alice", 30)
    print(alice.greet())
    
    alice.age = 31
    
def inheritance_and_polymorphism():
    print(inspect.currentframe().f_code.co_name)
    
    import abc
    
    class Animal(abc.ABC):
        @abc.abstractmethod
        def speak(self):
            raise NotImplementedError("サブクラスで実装してください")

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())  # DogはWoof!、CatはMeow!を出力

if __name__ == "__main__":
    #context_manager()
    #context_manager2()
    inheritance_and_polymorphism()
    