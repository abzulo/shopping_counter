def reset_stock():
    products["apple"]["stock"] = 50
    products["banana"]["stock"] = 100
    products["milk"]["stock"] = 20

def test_update_stock_success():
    reset_stock()
    result = update_stock("apple", 5)
    assert result == True
    assert products["apple"]["stock"] == 45

def test_update_stock_insufficient():
    reset_stock()
    result = update_stock("milk", 50)
    assert result == False
    assert products["milk"]["stock"] == 20  

def test_update_stock_invalid_product():
    reset_stock()
    result = update_stock("orange", 1)
    assert result == False