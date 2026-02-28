import inspect


def type_none():
    print(inspect.currentframe().f_code.co_name)
    print(bool(None == None))
    print(bool(None is None))
    print(bool(None == 0))
    print(bool(None is 0))
    print(bool(None == []))
    print(bool(None is []))
    print(bool(None))
    print(bool(0))
    print(bool([]))
    print(bool(""))
    print(bool(()))
    print(bool({}))
    print(bool(True))

    my_list = []

    if not my_list:
        print("The list is empty.")


def f_string():
    print(inspect.currentframe().f_code.co_name)
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    print(f"Next year, I will be {age + 1} years old.")
    print(f"Pi is approximately {3.14159:.2f}.")
    print(f"Binary representation of 10 is {10:b}.")
    print(f"Hexadecimal representation of 255 is {255:x}.")
    print(f"{3.14159:.2f}.")
    print(f"{3.14159:2f}.")

def list_and_array():
    print(inspect.currentframe().f_code.co_name)
    items = [1, "hello", True, None, 3.14]
    print(items)
    items.append("99")
    print(items.pop(), items)
    print(items.pop(0), items)
    
    items = [1, "hello", True, None, 3.14]
    print(items[0:3])
    print(items[::-2])
    
    nums = [10, 20, 30, 40, 50]

    # 以下の出力を予測してください
    print(nums[-2])
    print(nums[1:3])
    print(nums[::2])
    """
    `-1` が末尾（50）、`-2` がその一個手前（40）です。C#にはない概念なので最初は混乱しがちです。
    インデックスイメージ：
    10   20   30   40   50
    0    1    2    3    4   ← 正方向
    -5   -4   -3   -2   -1  ← 負方向
    """
    
def dictionary():
    print(inspect.currentframe().f_code.co_name)
    # 基本操作
    user = {"name": "Alice", "age": 30, "active": True}

    # 読み取り
    print(user["name"])          # Alice
    print(user.get("name"))      # Alice
    print(user.get("email"))     # None  ← KeyErrorにならない
    print(user.get("email", "")) # ""    ← デフォルト値指定

    # 追加・更新・削除
    user["email"] = "a@example.com"   # 追加
    user["age"] = 31                   # 更新
    del user["active"]                 # 削除

    # ループ（C#の foreach に相当）
    for key, value in user.items():    # dict.KeyValuePair
        print(f"{key}: {value}")

def tuple():
    print(inspect.currentframe().f_code.co_name)
    # タプル = イミュータブルなリスト（C#のreadonly配列に近い）
    #point[0] = 99   # TypeError！変更不可

    RGB_RED = (255, 0, 0)

    point = (10, 20)
    x, y = point
    print(x)   # 10
    print(y)   # 20

    # 関数から複数返り値（Pythonでよく使うパターン）
    def get_range(nums):
        return min(nums), max(nums)   # タプルで返す

    low, high = get_range([3, 1, 4, 1, 5])
    print(low, high)   # 1 5

    # _ で不要な値を捨てる
    first, _ = point   # yは使わない
    
    a, b = 1, 2
    b, a = a, b
    print(a, b)

def function():
    print(inspect.currentframe().f_code.co_name)
    
    # 基本形（C#のvoidメソッドに相当）
    def greet(name):
        print(f"Hello, {name}")

    # デフォルト引数（C#と同じ感覚）
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}")

    greet("Alice")            # Hello, Alice
    greet("Alice", "Hi")      # Hi, Alice

    # キーワード引数（C#の名前付き引数と同じ）
    greet(greeting="Hey", name="Bob")   # 順番を無視できる
    
    # 可変長引数
    def total(*args):
        return sum(args)
    
    # キーワード引数の可変長
    def dict_to_kwargs(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    print(total(10,20,30))
    
def lambda_func():
    print(inspect.currentframe().f_code.co_name)
    
    # 実践でよく使う場面：sorted のキー指定
    users = [
        {"name": "Carol", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Bob",   "age": 20},
    ]

    # ageでソート（C#のOrderBy(u => u.Age)に相当）
    sorted_users = sorted(users, key=lambda u: u["age"])
    print(sorted_users)
    # Bob(20) → Carol(25) → Alice(30)

    # 逆順
    sorted_users = sorted(users, key=lambda u: u["age"], reverse=True)


if __name__ == "__main__":
    #type_none()
    #f_string()
    #list_and_array()
    #dictionary()
    #tuple()
    #function()
    lambda_func()
    