print("f-strings")
# f-stringsのほうが新しく処理が早いらしいからこっちがいい
a = "a"
print(f"a is {a}")

x, y, z = 1, 2, 3
print(f"a is {x} {y} {z}")
print(f"a is {z} {y} {x}")

name = "Ryusuke"
family = "Yamada"
print(f"My name is {name} {family}. 私は {family} {name} です。")
print(f"My name is {name} {family}. 私は {family} {name} です。")
