from src.code import alphabet_position
import string
import random

def ap(text):
    text = text.lower().strip()
    return " ".join([str(ord(x) - ord("a")+1) for x in text if x in string.ascii_letters])

def test_upper_lower():
    assert alphabet_position("The sunset sets at twelve o' clock") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
def test_non_letters():
    assert alphabet_position("-,.'") == ""


    
def test_100_random():
    for i in range(100):
        x = ''.join(random.choice(string.ascii_letters) for _ in range(100))
        assert alphabet_position(x) == ap(x)