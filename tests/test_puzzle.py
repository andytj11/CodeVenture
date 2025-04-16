import pytest
from game_puzzle import WordSearchPuzzle


def setup_puzzle():
    return WordSearchPuzzle()


def test_check_word_positive():
    """Positive Test: Check if a valid word is correctly identified"""
    puzzle = setup_puzzle()
    assert puzzle.check_word("PYTHON") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("LIST") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("CLASS") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("FUNCTION") == True


def test_check_word_negative():
    """Negative Test: Check if an invalid word is correctly identified"""
    puzzle = setup_puzzle()
    assert puzzle.check_word("INVALID") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("PYTHONNNNN") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("$") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("123") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("....") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("VARIABLE") == False


def test_check_word_length():
    """Positive Test: Check if a valid word with length 3 is correctly identified"""
    puzzle = setup_puzzle()
    assert puzzle.check_word("FOR") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("AND") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("OR") == True

    """Negative Test: Check if a valid word with length 3 is not correctly identified"""
    puzzle = setup_puzzle()
    assert puzzle.check_word("NOT") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("IF") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("ELSE") == False


def test_search_positive():
    """Positive Test: Check if the search function finds a word correctly"""
    puzzle = setup_puzzle()
    assert puzzle.search("LIST", 1, 4) == True

    puzzle = setup_puzzle()
    assert puzzle.search("PYTHON", 0, 0) == True


def test_search_negative():
    """Negative Test: Check if the search function identifies an invalid word"""
    puzzle = setup_puzzle()
    assert puzzle.search("FAKE", 1, 4) == False

    puzzle = setup_puzzle()
    assert puzzle.search("FUNCTION", 4, 0) == False

    puzzle = setup_puzzle()
    assert puzzle.search("CLASS", 4, 0) == False


def test_check_word_diagonal_positive():
    """Positive Test: Check if a diagonal word is correctly identified"""
    puzzle = setup_puzzle()
    assert puzzle.check_word("CLASS") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("FUNCTION") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("PYTHON") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("LIST") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("LOOP") == True

    puzzle = setup_puzzle()
    assert puzzle.check_word("STRING") == True


def test_unknown_word_negative():
    """Negative Test: Check if a reversed word is correctly identified as not present"""
    puzzle = setup_puzzle()
    assert puzzle.check_word("....") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("VARIABLE") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("FLOAT") == False

    puzzle = setup_puzzle()
    assert puzzle.check_word("INTEGER") == False



