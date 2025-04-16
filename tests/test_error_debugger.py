import pytest
from error_debugger import ErrorHandling


def test_execute_code_success():
    """Positive Test: Check if a valid code executes successfully."""
    handler = ErrorHandling()
    code = "print('Hello, World!')"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "print('Hello, World!')\nprint('Hello, World!')"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "print('Hello, World!')\nprint('Hello, World!')\nprint('Hello, World!')"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None


def test_execute_code_unknown_error():
    """Positive Test for test_execute_code_unknown_error: Ensure no exceptions are raised."""
    handler = ErrorHandling()
    code = "print('Known error test')"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "print('Known error test')\nprint('Known error test')"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    """Negative Test: Check if an unknown error returns a generic suggestion."""
    handler = ErrorHandling()
    code = "raise Exception('Unknown error')"
    error, suggestion = handler.execute_code(code)
    assert "Unknown error" in error
    assert suggestion == 'Check the code for potential issues.'

    code = "raise Exception('Code execution failed')"
    error, suggestion = handler.execute_code(code)
    assert "Code execution failed" in error
    assert suggestion == 'Check the code for potential issues.'

    code = "raise Exception('Stack overflow')"
    error, suggestion = handler.execute_code(code)
    assert "Stack overflow" in error
    assert suggestion == 'Check the code for potential issues.'


def test_execute_code_syntax_error():
    """Positive Test for test_execute_code_syntax_error: Ensure code with correct syntax works."""
    handler = ErrorHandling()
    code = "print('Hello, World!')"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "print(True)"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "print(12345)"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "print(12.345)"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    """Negative Test: Check if a SyntaxError returns the correct suggestion."""
    handler = ErrorHandling()
    code = "prin(ndefined_variable)"
    error, suggestion = handler.execute_code(code)
    assert "name 'prin' is not defined" in error
    assert suggestion == 'Make sure all variables or functions are correctly defined and spelled.'

    code = "print(true)"
    error, suggestion = handler.execute_code(code)
    assert "name 'true' is not defined" in error
    assert suggestion == 'Make sure all variables or functions are correctly defined and spelled.'

    code = "print(_)"
    error, suggestion = handler.execute_code(code)
    assert "name '_' is not defined" in error
    assert suggestion == 'Make sure all variables or functions are correctly defined and spelled.'


def test_execute_code_type_error():
    """Positive Test for test_execute_code_type_error: Ensure code with correct data type works."""
    handler = ErrorHandling()
    code = "len('12345')"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "len([1, 2, 3, 4, 5])"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    """Negative Test: Check if a TypeError returns the correct suggestion."""
    handler = ErrorHandling()
    code = "len(12345)"
    error, suggestion = handler.execute_code(code)
    assert "object of type 'int' has no len()" in error
    assert suggestion == 'Check the types of your variables or the arguments in functions/methods.'

    code = "len(12.345)"
    error, suggestion = handler.execute_code(code)
    assert "object of type 'float' has no len()" in error
    assert suggestion == 'Check the types of your variables or the arguments in functions/methods.'


def test_execute_code_name_error():
    """Positive Test for test_execute_code_name_error: Ensure code with correctly defined variable works."""
    handler = ErrorHandling()
    code = "variable = 'Hello'\nprint(variable)"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    code = "variable = 12345\nprint(variable)"
    error, suggestion = handler.execute_code(code)
    assert error == "Code executed successfully!"
    assert suggestion == None

    """Negative Test: Check if a NameError returns the correct suggestion."""
    handler = ErrorHandling()
    code = "print(unknown_variable)"
    error, suggestion = handler.execute_code(code)
    assert "name 'unknown_variable' is not defined" in error
    assert suggestion == 'Make sure all variables or functions are correctly defined and spelled.'

    code = "print(unknown_variable + 1)"
    error, suggestion = handler.execute_code(code)
    assert "name 'unknown_variable' is not defined" in error
    assert suggestion == 'Make sure all variables or functions are correctly defined and spelled.'