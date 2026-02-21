def test_one():
    print("ПРИВЕТ! Этот тест работает!")
    assert 1 + 1 == 2

def test_two():
    assert "hello".upper() == "HELLO"