from farewell import on_exit

def test_on_exit():
    on_exit(lambda: None, lambda: None)
