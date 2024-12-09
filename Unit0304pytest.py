import Unit0303pytest as u


def showError():
    u.testError()
    assert "變數無定義"


def showRemove():
    u.restRemove()
    assert "找不到myfolder資料夾"


showError()
showRemove()
