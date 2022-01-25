import spam_detector

def test1():
    email = "today@promo.com"
    assert spam_detector.detect_spam(email) == 1.0

def test2():
    email = "example@mail.cn"
    assert spam_detector.detect_spam(email) == 0.25

def test3():
    email = "example123@mail.cn"
    assert spam_detector.detect_spam(email) == 0.50

def test4():
    email ="example@mail123.cn"
    assert spam_detector.detect_spam(email) == 0.50

def test5():
    email = "example@ma.il.com"
    assert spam_detector.detect_spam(email) == 0.50

def test6():
    email = "example@ma-il.com"
    assert spam_detector.detect_spam(email) == 0.50

def test7():
    email = "example123@ma-il.cn"
    assert spam_detector.detect_spam(email) == 1.0

test1()
test2()
test3()
test4()
test5()
test6()
test7()