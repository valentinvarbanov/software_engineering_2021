from password import weak_passwords, letters_password, special_letters_password, size_password

def test_weak_password_true():
    weak_pass = ['12345', 'qwerty', 'password', 'asdf']
    for weak in weak_pass:
        assert weak_passwords(weak) == True

def test_letters_password():
    assert letters_password("a") == True
    assert letters_password("asdfghj") == True
    assert letters_password("zkjhgfvh") == True
    assert letters_password("1232") == False
    assert letters_password("elsys") == True

def test_special_letters_password():
    assert special_letters_password("a") == False
    assert special_letters_password("!") == True
    assert special_letters_password("afgh*") == True
    assert special_letters_password("el$y$") == True

def test_size_password():
    assert size_password("adfghjsdfghjkjhgfd") == True
    assert size_password("abcdiefs") == False
    assert size_password("a") == False

# def test_all()
#     assert 