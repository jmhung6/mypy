# 自訂函數
def favorite(name):
    print("你最愛的咖啡是:", name)


def sale(name, price, qty):
    print(
        "咖啡名稱:%s\n價格:%3d\n數量:%3d\n合計:%4d元" % (name, price, qty, price * qty)
    )
