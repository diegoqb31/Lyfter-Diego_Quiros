from Ejercicios_Funciones import count_uppercase_lowercase

def test_count_uppercase_lowercase_mixed():
    assert count_uppercase_lowercase("HelloWorld") == (2, 8)


def test_count_uppercase_lowercase_all_upper():
    assert count_uppercase_lowercase("HELLO") == (5, 0)


def test_count_uppercase_lowercase_all_lower():
    assert count_uppercase_lowercase("hello") == (0, 5)