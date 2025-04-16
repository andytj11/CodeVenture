import pytest
from mock_ai import MockAI


def test_generate_sample_code():
    """Positive Test: Check if the generate_sample_code method returns a list of samples."""
    samples = MockAI.generate_sample_code()

    assert isinstance(samples, list)

    assert len(samples) > 0

    assert "print('Hello, World!')" in samples


def test_suggest_code_positive():
    """Positive Test: Check if the suggest_code method returns a relevant suggestion."""
    suggestion = MockAI.suggest_code("for i in range(len(some_list))")
    assert suggestion == "Consider using 'for item in some_list' for a more Pythonic loop."

    suggestion = MockAI.suggest_code("for i in range(len(some_list)):\n\tprint(some_list[i])")
    assert suggestion == "Consider using 'for item in some_list' for a more Pythonic loop."

    suggestion = MockAI.suggest_code("for i in range(len(some_list)):\n\tprint(some_list[i])\nprint('Hello, World!')")
    assert suggestion == "Consider using 'for item in some_list' for a more Pythonic loop."


def test_suggest_code_negative():
    """Negative Test: Check if the suggest_code method returns a default message when unable to suggest."""
    suggestion = MockAI.suggest_code("some_random_code")
    assert suggestion == "Can't provide suggestions for this specific code."

    suggestion = MockAI.suggest_code("some_random_code\nsome_random_code")
    assert suggestion == "Can't provide suggestions for this specific code."

    suggestion = MockAI.suggest_code("some_random_code\nsome_random_code\nsome_random_code")
    assert suggestion == "Can't provide suggestions for this specific code."


def test_explain_code_positive():
    """Positive Test: Check if the explain_code method provides a relevant explanation."""
    explanation = MockAI.explain_code("numbers.append(5)")
    assert explanation == "This code is adding an item to a list."

    explanation = MockAI.explain_code("numbers.append(5)\nnumbers.append(6)")
    assert explanation == "This code is adding an item to a list."

    explanation = MockAI.explain_code("numbers.append(5)\nnumbers.append(6)\nnumbers.append(7)")
    assert explanation == "This code is adding an item to a list."


def test_explain_code_negative():
    """Negative Test: Check if the explain_code method returns a default message when unable to explain."""
    explanation = MockAI.explain_code("some_unknown_function()")
    assert explanation == "Can't provide an explanation for this code."

    explanation = MockAI.explain_code("youtuberbang()\nyoutuberbang()")
    assert explanation == "Can't provide an explanation for this code."

    explanation = MockAI.explain_code(".()))")
    assert explanation == "Can't provide an explanation for this code."


def test_format_code():
    """Positive Test: Check if the format_code method returns a formatted version of the input code."""
    formatted_code = MockAI.format_code("print( 1 , 2 , 3 )")
    assert formatted_code == "print( 1, 2, 3 )"

    formatted_code = MockAI.format_code("print(1,2,3)")
    assert formatted_code == "print(1,2,3)"



