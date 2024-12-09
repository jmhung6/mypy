import os


def testError():
    try:
        print(f"j={j}")
    except:
        print("變數未定義")
    print("hello")


def restRemove():
    try:
        os.rmdir("myfolder")
        print("myfloder資料及已刪除")
    except:
        print("找不到folder資料夾")
    print("hello2")
