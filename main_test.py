from main import convert_num_to_word, convert_expression_to_words


# Test convert_num_to_word function
def test_convert_num_to_word_1():
    assert convert_num_to_word(123) == "one hundred twenty-three"


def test_convert_num_to_word_2():
    assert convert_num_to_word(
        132123) == "one hundred thirty-two thousand one hundred twenty-three"


def test_convert_num_to_word_3():
    assert convert_num_to_word(
        2111111) == "two million one hundred eleven thousand one hundred eleven"


def test_convert_num_to_word_4():
    assert convert_num_to_word(
        9999) == "nine thousand nine hundred ninety-nine"


def test_convert_num_to_word_5():
    assert convert_num_to_word(10000001) == "ten million one"


# Test convert_expression_to_words() function
def test_convert_expression_to_words_1():
    assert convert_expression_to_words("4+4=") == "Invalid input"


def test_convert_expression_to_words_2():
    assert convert_expression_to_words(
        "123+22=145") == "one hundred twenty-three plus twenty-two equals one hundred forty-five"


def test_convert_expression_to_words_3():
    assert convert_expression_to_words(
        "99+1=100") == "ninety-nine plus one equals one hundred "


def test_convert_expression_to_words_4():
    assert convert_expression_to_words(
        "99+5=104") == "ninety-nine plus five equals one hundred four"


def test_convert_expression_to_words_5():
    assert convert_expression_to_words("25.0+1=26") == "Invalid input"
