class User:
    count = 0              # クラスフィールド

    def __init__(self):
        self.name = ""
        self.count = 100   # インスタンスフィールドを生やしている
        
# Pythonの構文に直すと
u = User()
print(User.count)   # ?
print(u.count)      # ?
User.count=200
print(User.count)   # ?
print(u.count)      # ?