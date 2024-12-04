import os

"""


"""

# Exception
try:
    print(f"j={j}")
except:
    print("未定義")
print("Hello")

try:
    os.rmdir("myfolder")
    print("Myfolder資料夾已刪除")
except:
    print("Not found myfolder")
print("Hello")
