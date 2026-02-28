# Python習得 総復習

> C#エンジニア向け・実務直結のPythonまとめ

---

## 目次

1. [Python思想：明示・シンプル・信頼](#1-python思想明示シンプル信頼)
2. [型：名札とオブジェクト](#2-型名札とオブジェクト)
3. [コレクション：スライスとアンパック](#3-コレクションスライスとアンパック)
4. [関数：第一級オブジェクト](#4-関数第一級オブジェクト)
5. [デコレータ：インターセプター](#5-デコレータインターセプター)
6. [クラス：紳士協定のOOP](#6-クラス紳士協定のoop)
7. [型ヒントとPydantic](#7-型ヒントとpydantic)
8. [非同期：待ち時間を重ねる](#8-非同期待ち時間を重ねる)
9. [FastAPI：全部の集大成](#9-fastapi全部の集大成)
10. [まとめ：C#エンジニアがPythonで意識すること](#10-まとめcエンジニアがpythonで意識すること)

---

## 1. Python思想：明示・シンプル・信頼

C#はコンパイラがプログラマを守ります。型が違えばコンパイルエラー、アクセス修飾子で隠蔽を強制。Pythonは逆で「ちゃんと書けるでしょ」という信頼ベースの設計です。アクセス修飾子はなく、型チェックも強制されません。

```python
# Pythonは「大人同士の紳士協定」で成り立つ
self._age = 30    # privateのつもり、でも強制ではない
self.__id = 99    # より強い意思表示、でもやはり強制ではない
```

### アンダースコアの種類

| 記法 | 意味 | C#相当 |
|---|---|---|
| `name` | パブリック | `public` |
| `_name` | プライベート慣習（紳士協定） | `private`（強制なし） |
| `__name` | 名前マングリング（より強い隠蔽） | `private` |
| `__name__` | ダンダー（Pythonの予約済み） | 予約語 |
| `_` | 使い捨て変数 | `_`（C#と同じ） |

### 命名規則

| 種類 | Python | C# |
|---|---|---|
| 変数・関数 | `snake_case` | `camelCase` |
| クラス | `PascalCase` | `PascalCase` |
| 定数 | `UPPER_SNAKE` | `UPPER_SNAKE` |

### よく使うダンダー

```python
__init__     # コンストラクタ
__str__      # print()したときの文字列表現（ToString()相当）
__repr__     # デバッグ用文字列表現
__len__      # len()で呼ばれる
__eq__       # == 演算子
__add__      # + 演算子
__enter__    # withブロック開始
__exit__     # withブロック終了
```

---

## 2. 型：名札とオブジェクト

C#の変数は「型を持つ箱」。Pythonの変数は「オブジェクトへの名札」です。

```python
x = 42        # 名札xをintオブジェクト42に貼る
x = "hello"   # 名札xをstrオブジェクトに貼り替える
x = [1,2,3]   # 名札xをlistオブジェクトに貼り替える
```

### Falsy（偽とみなされる値）

```python
# 以下は全てbool評価でFalse
None, 0, "", [], {}, (), 0.0

# 実践でよく使う
if not items:       # 空リスト・None・空文字を一括チェック
    return

if value is None:   # Noneのチェックはis Noneを使う（== Noneは非Pythonic）
    return
```

### f-string（C#の`$""`に相当）

```python
name = "Alice"
score = 95

print(f"{name}は{score}点")      # Alice は95点
print(f"{score:.2f}")            # 95.00（小数点2桁）
print(f"{score:,}")              # 1,234,567（カンマ区切り）
print(f"{name:>10}")             # '     Alice'（右寄せ10文字）
```

---

## 3. コレクション：スライスとアンパック

### リスト

```python
items = [1, 2, 3, 4, 5]

# 基本操作
items.append(6)     # 末尾追加（list.Add()）
items.pop()         # 末尾削除
items.pop(0)        # 先頭削除
len(items)          # 要素数（list.Count）

# スライス（C#にない概念）
items[1:4]          # [2, 3, 4]（インデックス1〜3）
items[:3]           # [1, 2, 3]（先頭から3つ）
items[-1]           # 5（末尾 = 地下1階）
items[-2]           # 4（末尾から2番目 = 地下2階）
items[::-1]         # [5, 4, 3, 2, 1]（逆順）
```

### 辞書（C#の`Dictionary<K,V>`に相当）

```python
user = {"name": "Alice", "age": 30}

# 読み取り
user["name"]              # Alice（キーがなければKeyError）
user.get("name")          # Alice（キーがなければNone）
user.get("email", "")     # ""（デフォルト値指定）

# ループ
for key, value in user.items():
    print(f"{key}: {value}")
```

### タプルとアンパック

```python
# タプル = イミュータブルなリスト
point = (10, 20)
point[0] = 99   # TypeError！変更不可

# アンパック
x, y = point
a, b = b, a     # temp変数なしで入れ替え

# 使い捨て変数
first, _ = point   # 2番目は使わない
```

### 内包表記

```python
# list comprehension
squares = [x**2 for x in range(10)]

# 条件付き
evens = [x for x in range(10) if x % 2 == 0]

# dict comprehension
d = {k: v for k, v in items.items() if v > 0}

# generator（遅延評価・省メモリ）
squares_gen = (x**2 for x in range(10))
```

---

## 4. 関数：第一級オブジェクト

### 基本

```python
# デフォルト引数の罠（ミュータブルはNG）
def append_item(item, lst=[]):   # NG：lstが共有される
    lst.append(item)
    return lst

def append_item(item, lst=None): # OK
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# キーワード引数（C#の名前付き引数と同じ）
greet(greeting="Hey", name="Bob")

# 可変長引数
def total(*args):           # タプルで受け取る
    return sum(args)

def profile(**kwargs):      # 辞書で受け取る
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### lambda

```python
# C#のラムダ式と同じ
double = lambda x: x * 2

# よく使う場面：sortedのキー指定
sorted(users, key=lambda u: u["age"])
sorted(words, key=len)   # 関数オブジェクトをそのまま渡せる
```

### クロージャ

「生まれた環境を記憶した関数」。C#でプライベートフィールドを持つクラスを作る場面を軽量に実現します。

```python
def make_tax_calculator(tax_rate):
    def calculate(price):
        return price * (1 + tax_rate)   # tax_rateを記憶
    return calculate

calc_jp = make_tax_calculator(0.10)   # 消費税10%を焼き込んだ計算機
calc_jp(1000)   # 1100.0

# nonlocal：外のスコープの変数を書き換える
def counter(start=0):
    count = start
    def increment():
        nonlocal count   # 読むだけならnonlocal不要、書き換えるなら必要
        count += 1
        return count
    return increment
```

---

## 5. デコレータ：インターセプター

C#のMiddlewareやAOPインターセプターと同じ思想。正体はクロージャ。

```python
# 基本構造
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} 開始")   # 前処理
        result = func(*args, **kwargs)   # 本来の関数
        print(f"{func.__name__} 終了")   # 後処理
        return result
    return wrapper

@logger   # = greet = logger(greet)
def greet(name):
    print(f"Hello, {name}")
```

### よく使うデコレータ

```python
# 実行時間計測
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - start:.3f}秒")
        return result
    return wrapper

# キャッシュ（標準ライブラリ）
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### コンテキストマネージャ（C#の`using`に相当）

```python
# withブロックを抜けると例外が発生しても必ずクリーンアップが走る
with open("file.txt") as f:
    data = f.read()

# 自作する場合
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield               # withブロックの中身
    finally:
        print(f"{time.time() - start:.3f}秒")   # 必ず実行

with timer():
    time.sleep(1)
```

---

## 6. クラス：紳士協定のOOP

### 3種類のメソッド

```python
class Dog:
    count = 0              # クラスフィールド（staticフィールド）

    def __init__(self):
        self.name = ""     # インスタンスフィールド（self.xxxで定義）

    def bark(self):        # インスタンスメソッド
        return "ワン"

    @classmethod
    def get_count(cls):    # クラスメソッド：クラスフィールドにアクセスする
        return cls.count   # cls = クラスそのもの（継承時に便利）

    @staticmethod
    def description():     # スタティックメソッド：状態不要なユーティリティ
        return "犬クラスです"
```

### プロパティ（C#の`{ get; set; }`に相当）

```python
class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):              # getter
        return self._age

    @age.setter
    def age(self, value):       # setter
        if value < 0:
            raise ValueError("年齢は0以上")
        self._age = value

u = User(30)
print(u.age)   # 30（メソッドなのに()不要）
u.age = 31     # setterが呼ばれる
```

### 継承

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):           # C#の : Animal に相当
    def __init__(self, name, breed):
        super().__init__(name)   # 親の__init__を明示的に呼ぶ（必須）
        self.breed = breed

    def speak(self):
        base = super().speak()   # C#のbase.Speak()
        return f"{base}（犬）"
```

### 抽象クラス

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):   # 必ずオーバーライドしないとエラー
        pass

# Animal()   # TypeError！インスタンス化できない
```

### ダンダーメソッド（演算子オーバーロード）

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):     # print()したときの表示（ユーザー向け）
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):    # デバッグ用（開発者向け）
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):   # + 演算子
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):    # == 演算子
        return self.x == other.x and self.y == other.y
```

### dataclass（C#のrecordに相当）

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int = 0
    tags: list = field(default_factory=list)
    # __init__ / __repr__ / __eq__ が自動生成される

@dataclass(frozen=True)   # イミュータブル
class Point:
    x: float
    y: float
```

---

## 7. 型ヒントとPydantic

### 型ヒント

**飾りです。実行時に強制されません。** IDEの補完とmypyによる静的解析のためのヒントです。

```python
def greet(name: str, age: int) -> str:
    return f"{name}は{age}歳"

# Noneを許容する（C#のnullable相当）
def find_user(id: int) -> str | None:   # Python3.10以降
    return None

# コレクション
def process(items: list[int]) -> dict[str, int]:
    return {"count": len(items)}
```

```bash
# 静的解析（C#のコンパイラ相当）
pip install mypy
mypy myfile.py
```

### Pydantic（実行時バリデーション）

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("年齢は0以上")
        return v

User(name="Alice", age="30")    # "30"→30に自動変換
User(name="Alice", age="abc")   # ValidationError！
```

| | dataclass | Pydantic |
|---|---|---|
| バリデーション | なし | あり |
| 型変換 | なし | あり（"30"→30） |
| 用途 | 内部モデル | APIリクエスト・設定 |
| ライブラリ | 標準 | 外部 |

---

## 8. 非同期：待ち時間を重ねる

PythonはGIL（Global Interpreter Lock）によりシングルスレッドしかCPUを使えません。そのため非同期は「並列実行」ではなく「待ち時間を重ねる」仕組みです。

```python
import asyncio

# C#のasync/awaitとほぼ同じ構文
async def fetch_user():
    await asyncio.sleep(2)   # I/O待ちのシミュレーション
    return "Alice"

async def main():
    # asyncio.gather = C#のTask.WhenAll()
    user, order = await asyncio.gather(
        fetch_user(),    # 2秒待ち
        fetch_order(),   # 2秒待ち
    )
    # 合計2秒で終わる

asyncio.run(main())   # イベントループを起動
```

### 向き・不向き

```
向いている   → API呼び出し・DB待ち・ファイルI/O
向いていない → 画像処理・機械学習・重い計算（→ multiprocessing）
```

### 並行・並列の使い分け

| 目的 | 手段 |
|---|---|
| I/O待ちを重ねる | `asyncio` |
| I/O待ちをスレッドで | `threading` |
| CPU処理を並列化 | `multiprocessing` |
| 両方いい感じに | `concurrent.futures` |

### ご法度パターン

```python
# ① async関数の中でブロッキング処理を呼ぶ
async def fetch():
    time.sleep(2)           # NG：イベントループ全体が止まる
    await asyncio.sleep(2)  # OK

# ② awaitを忘れる
async def main():
    fetch()        # NG：実行されない
    await fetch()  # OK

# ③ async関数の中でasyncio.run()を呼ぶ
async def main():
    asyncio.run(fetch())   # NG：イベントループが二重起動
```

### ブロッキングになる処理と代替

| ブロッキング（NG） | 非同期版（OK） |
|---|---|
| `time.sleep()` | `asyncio.sleep()` |
| `requests.get()` | `httpx.AsyncClient` / `aiohttp` |
| `open()` | `aiofiles` |
| `psycopg2` | `asyncpg` |

---

## 9. FastAPI：全部の集大成

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):        # Pydantic（バリデーション）
    name: str
    age: int

users: dict[int, User] = {}
counter = 0

# GET
@app.get("/users/{user_id}")  # デコレータ（ルーティング）
async def get_user(           # 非同期
    user_id: int              # 型ヒント（自動バリデーション）
) -> User:                    # レスポンス型
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Not Found")
    return users[user_id]

# POST
@app.post("/users")
async def create_user(user: User) -> dict:
    global counter
    counter += 1
    users[counter] = user
    return {"id": counter}

# PUT
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User) -> User:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Not Found")
    users[user_id] = user
    return users[user_id]

# DELETE
@app.delete("/users/{user_id}")
async def delete_user(user_id: int) -> dict:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Not Found")
    users.pop(user_id)
    return {"message": "削除しました"}
```

```bash
# 起動
uvicorn main:app --reload

# Swagger UI（自動生成）
http://127.0.0.1:8000/docs
```

### VSCode デバッグ設定（launch.json）

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "FastAPI Debug",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": ["main:app", "--reload"],
            "cwd": "${workspaceFolder}/python/fastapi"
        }
    ]
}
```

---

## 10. まとめ：C#エンジニアがPythonで意識すること

| C#の感覚 | Pythonの感覚 |
|---|---|
| コンパイラが守る | 紳士協定で守る |
| interfaceで型を保証 | ダックタイピングで柔軟に |
| 全部asyncにする | I/O待ちだけasync |
| クラスで状態を持つ | クロージャでも状態を持てる |
| 型は箱 | 型は名札 |
| `null` チェック | `if not value:` で統一 |
| `static` 1種類 | `classmethod` / `staticmethod` 2種類 |
| `Task` は本当の並列 | `asyncio.Task` は待ち時間の重ね合わせ |

Pythonは「制約が少ない分、書き手の意図と慣習が重要な言語」です。C#の経験があるからこそ、その慣習の意味が深く理解できます。

---

> 作成日：2026年2月  
> 対象：C#経験者向けPython中級-上級習得まとめ